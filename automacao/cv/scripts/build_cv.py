#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
build_cv.py
- Lê html/resume.html
- Extrai <header class="page-hero pdf1">...</header>
- Monta <main id="conteudo"> com SOMENTE os blocos marcados com classe pdfN (pdf2, pdf3, ...)
  ordenados pelo número.
- Injeta header + main no automacao/cv/templates/cv-print.html
- Gera PDF em assets/file/Curriculo_Hirlei_Carlos_RH_YYYYMMDD_HHMM.pdf
- NÃO atualiza arquivo fixo (só se usar --latest)

Requisitos:
- Python 3.10+
- weasyprint        (pip install weasyprint)
- beautifulsoup4    (pip install beautifulsoup4)
"""

from __future__ import annotations

import argparse
import re
import shutil
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

try:
    from zoneinfo import ZoneInfo
except ImportError:
    ZoneInfo = None  # type: ignore


@dataclass(frozen=True)
class Paths:
    root: Path
    resume_html: Path
    template_html: Path
    css_print: Path
    out_dir: Path


PDF_CLASS_RE = re.compile(r"^pdf(\d+)$", re.IGNORECASE)


def _project_root_from_here() -> Path:
    # .../automacao/cv/scripts/build_cv.py -> root é 3 níveis acima de scripts
    return Path(__file__).resolve().parents[3]


def _default_paths(root: Path) -> Paths:
    return Paths(
        root=root,
        resume_html=root / "html" / "resume.html",
        template_html=root / "automacao" / "cv" / "templates" / "cv-print.html",
        css_print=root / "automacao" / "cv" / "styles" / "cv-print.css",
        out_dir=root / "assets" / "file",
    )


def _read_text(path: Path) -> str:
    if not path.exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {path}")
    return path.read_text(encoding="utf-8", errors="strict")


def _now_sp() -> datetime:
    """
    Retorna data/hora em America/Sao_Paulo quando possível.
    Se o Windows não tiver tzdata/zoneinfo, cai para hora local.
    """
    if ZoneInfo is not None:
        try:
            return datetime.now(ZoneInfo("America/Sao_Paulo"))
        except Exception:
            pass
    return datetime.now()


def _safe_write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8", errors="strict")


def _generate_pdf(rendered_html_path: Path, css_path: Path, output_pdf: Path, base_url: Path) -> None:
    try:
        from weasyprint import HTML, CSS
    except Exception as e:
        raise RuntimeError("WeasyPrint não está disponível. Instale com: pip install weasyprint") from e

    output_pdf.parent.mkdir(parents=True, exist_ok=True)
    html = HTML(filename=str(rendered_html_path), base_url=str(base_url))
    css = CSS(filename=str(css_path))
    html.write_pdf(str(output_pdf), stylesheets=[css])


def _parse_html(html: str):
    try:
        from bs4 import BeautifulSoup
    except Exception as e:
        raise RuntimeError("BeautifulSoup não está disponível. Instale com: pip install beautifulsoup4") from e
    return BeautifulSoup(html, "html.parser")


def _has_pdf_class(tag) -> tuple[bool, int | None]:
    """
    Retorna (True, N) se o elemento tiver classe pdfN.
    """
    classes = tag.get("class") or []
    for c in classes:
        m = PDF_CLASS_RE.match(str(c))
        if m:
            return True, int(m.group(1))
    return False, None


def _parent_has_pdf_class(tag) -> bool:
    """
    Verifica se algum ancestral já tem classe pdfN (para evitar pegar pdf dentro de pdf).
    """
    p = tag.parent
    while p is not None and getattr(p, "name", None) is not None:
        ok, _n = _has_pdf_class(p)
        if ok:
            return True
        p = p.parent
    return False


def _extract_header_hero_and_main_pdf_blocks(resume_html: str) -> tuple[str, str]:
    """
    - Extrai <header class="page-hero pdf1">...</header> inteiro
    - Monta um <main id="conteudo">...</main> NOVO contendo SOMENTE os blocos pdfN, ordenados.
    """
    soup = _parse_html(resume_html)

    def has_any_class(tag, expected: tuple[str, ...]) -> bool:
        classes = tag.get("class") or []
        return any(c in classes for c in expected)

    header = soup.find(lambda tag: getattr(tag, "name", None) == "header" and has_any_class(tag, ("pdf1", "page-hero", "hero")))
    if not header:
        raise ValueError('Não encontrei <header class="page-hero pdf1"> no resume.html')

    for item in header.select(".page-hero__contact-item"):
        for child in list(item.children):
            if getattr(child, "name", None) is None:
                child.replace_with(re.sub(r"^[^A-Za-zÀ-ÿ0-9+]+", "", str(child)).lstrip())
                break

    main = soup.find("main", id="conteudo")
    if not main:
        raise ValueError('Não encontrei <main id="conteudo"> no resume.html')

    # remove footer interno do main, se existir
    for f in main.find_all("footer", class_=lambda v: v and "footer" in (v if isinstance(v, list) else str(v).split())):
        f.decompose()

    # pega TODOS os elementos dentro do main que tenham pdfN
    candidates = main.find_all(True, class_=lambda v: v and any(PDF_CLASS_RE.match(str(x)) for x in (v if isinstance(v, list) else str(v).split())))

    blocks: list[tuple[int, object]] = []

    for tag in candidates:
        ok, n = _has_pdf_class(tag)
        if not ok or n is None:
            continue

        # evita pegar coisas "pdf" dentro de outra coisa "pdf"
        if _parent_has_pdf_class(tag):
            continue

        blocks.append((n, tag))

    # ordena por N
    blocks.sort(key=lambda x: x[0])

    # monta um main NOVO preservando a tag de abertura original (classes etc)
    new_main = soup.new_tag("main")
    new_main.attrs = dict(main.attrs)  # mantém id, class, etc.

    for _n, tag in blocks:
        # move o elemento para o new_main
        new_main.append(tag)

    header_html = str(header)
    main_html = str(new_main)

    return header_html, main_html


def _inject_header_and_main(template_html: str, header_html: str, main_html: str) -> str:
    """
    Substitui no template:
    - o <header class="hero">...</header> pelo header do resume
    - o <main id="conteudo">...</main> pelo main montado (pdfN)
    """
    rendered, n1 = re.subn(
        r'<header\b[^>]*class=["\'][^"\']*\b(?:hero|page-hero)\b[^"\']*["\'][^>]*>.*?</header\s*>',
        header_html,
        template_html,
        flags=re.IGNORECASE | re.DOTALL,
        count=1,
    )
    if n1 != 1:
        raise ValueError("Não consegui substituir o <header> no cv-print.html")

    rendered2, n2 = re.subn(
        r'<main\b[^>]*\bid=["\']conteudo["\'][^>]*>.*?</main\s*>',
        main_html,
        rendered,
        flags=re.IGNORECASE | re.DOTALL,
        count=1,
    )
    if n2 != 1:
        raise ValueError("Não consegui substituir o <main id='conteudo'> no cv-print.html")

    return rendered2


def main() -> int:
    root = _project_root_from_here()
    p = _default_paths(root)

    parser = argparse.ArgumentParser(description="Gerar PDF do currículo a partir do resume.html (ordenando pdfN)")
    parser.add_argument("--resume", type=str, default=str(p.resume_html))
    parser.add_argument("--template", type=str, default=str(p.template_html))
    parser.add_argument("--css", type=str, default=str(p.css_print))
    parser.add_argument("--outdir", type=str, default=str(p.out_dir))
    parser.add_argument("--prefix", type=str, default="Curriculo_Hirlei_Carlos_RH")
    parser.add_argument("--latest", action="store_true", help="(Opcional) Atualizar também o arquivo fixo prefix.pdf")
    args = parser.parse_args()

    resume_path = Path(args.resume).resolve()
    template_path = Path(args.template).resolve()
    css_path = Path(args.css).resolve()
    out_dir = Path(args.outdir).resolve()
    prefix = args.prefix.strip()

    resume_html = _read_text(resume_path)
    template_html = _read_text(template_path)

    header_html, main_html = _extract_header_hero_and_main_pdf_blocks(resume_html)

    rendered_html = _inject_header_and_main(template_html, header_html, main_html)

    tmp_dir = template_path.parent / ".tmp"
    tmp_dir.mkdir(parents=True, exist_ok=True)
    rendered_path = tmp_dir / "cv-rendered.html"
    _safe_write(rendered_path, rendered_html)

    ts = _now_sp().strftime("%Y%m%d_%H%M")
    out_pdf_timestamped = out_dir / f"{prefix}_{ts}.pdf"
    out_pdf_latest = out_dir / f"{prefix}.pdf"

    _generate_pdf(rendered_path, css_path, out_pdf_timestamped, base_url=root)

    if args.latest:
        shutil.copyfile(out_pdf_timestamped, out_pdf_latest)

    print("OK")
    print(f"Gerado: {out_pdf_timestamped}")
    if args.latest:
        print(f"Atualizado: {out_pdf_latest}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
