# 👨‍💻 Hirlei Carlos — Portfólio Profissional & Sistema Automatizado de Currículo

![Status](https://img.shields.io/badge/status-ativo-success)
![Stack](https://img.shields.io/badge/stack-HTML%20%7C%20CSS%20%7C%20Python-blue)
![PDF Engine](https://img.shields.io/badge/PDF-WeasyPrint-orange)
![Hospedagem](https://img.shields.io/badge/hosting-GitHub%20Pages-black)
![Redesign](https://img.shields.io/badge/redesign-2026-red)

---

## 📌 Visão Geral

Este repositório contém:

- 🌐 Site profissional estático — completamente redesenhado em 2026
- 📄 Currículo online (HTML) com sistema de geração de PDF automatizado
- 🖨 Motor de geração de PDF via Python + WeasyPrint
- 🧠 Ordenação semântica de seções via classes `pdfN`
- 🚀 Hospedagem via GitHub Pages

O projeto separa completamente:

- **Camada de apresentação Web** — HTML + CSS responsivo
- **Camada de impressão (PDF)** — template isolado + CSS de impressão
- **Camada de processamento** — Python + BeautifulSoup

---

## 📁 Estrutura do Projeto

```
hirleicarlos.github.io/
│
├── index.html                              ← Home
│
├── html/
│   ├── projects.html                       ← Cases & Atuação
│   ├── resume.html                         ← Currículo (fonte do PDF)
│   ├── articles.html                       ← Artigos & Newsletter
│   ├── sistemaocb.html                     ← Case: Sistema OCB
│   ├── cmsjoomla.html                      ← Case: Engenharia Joomla
│   └── ufg.html                            ← Case: UFG
│
├── assets/
│   ├── css/
│   │   ├── variaveis.css                   ← Tokens globais de design
│   │   ├── global.css                      ← Reset, navbar, footer, botões, tags
│   │   ├── home.css                        ← Exclusivo da home
│   │   ├── projects.css                    ← Exclusivo de Cases & Atuação
│   │   ├── resume.css                      ← Exclusivo do currículo
│   │   ├── articles.css                    ← Exclusivo de artigos
│   │   └── subpage.css                     ← Compartilhado: sistemaocb, cmsjoomla, ufg
│   ├── js/
│   │   ├── nav.js                          ← Navbar responsiva
│   │   ├── main.js
│   │   └── masonry.js
│   ├── img/
│   │   ├── site/                           ← favicon.ico, favicon.svg, icon_hirlei.svg, logo_hirlei.svg
│   │   ├── case/                           ← Imagens dos projetos (.webp)
│   │   ├── artigos/                        ← Capas Dev & Versos (.png)
│   │   ├── hirlei.jpg                      ← Foto do perfil
│   │   └── social.png                      ← Imagem Open Graph (1200×630)
│   └── file/
│       ├── Curriculo_Hirlei_Carlos_RH.pdf  ← Versão fixa (atualizada com --latest)
│       └── Curriculo_Hirlei_Carlos_RH_YYYYMMDD_HHMM.pdf  ← Versionado por data/hora
│
├── automacao/
│   └── cv/
│       ├── scripts/
│       │   └── build_cv.py                 ← Script Python de geração do PDF
│       ├── templates/
│       │   ├── cv-print.html               ← Template de impressão
│       │   └── .tmp/cv-rendered.html       ← HTML intermediário (gerado automaticamente)
│       └── styles/
│           └── cv-print.css                ← CSS exclusivo para PDF
│
└── updates/
    ├── mod_hc_socialmedia.xml                  ← Update server: módulo HC Mídias Sociais
    ├── mod_hc_igpulse.xml                     ← Update server: módulo HC IgPulse
    ├── pkg_hcimageoptimizer.xml               ← Update server: pacote HC Image Optimizer
    ├── plg_media-action_hcimageoptimizer.xml  ← Update server: integração do Gerenciador de Mídia
    ├── plg_system_btnwhatsapp.xml             ← Update server: plugin WhatsApp flutuante
    ├── plg_system_hcimageoptimizer.xml        ← Update server: plugin HC Image Optimizer
    └── tpl_hc_carlix.xml                      ← Update server: template HC Carlix
```

---

## 🎨 Design System — variaveis.css

Todos os arquivos CSS importam `variaveis.css` como fonte única de tokens.

### Marca

| Token | Valor |
|-------|-------|
| `--red` | `#C41E20` |
| `--red-dark` | `#8B1010` |
| `--red-bg` | `rgba(196, 30, 32, 0.07)` |
| `--red-border` | `rgba(196, 30, 32, 0.20)` |
| `--red-shadow` | `0 8px 24px rgba(196, 30, 32, 0.22)` |

### Neutros

| Token | Valor |
|-------|-------|
| `--bg` | `#F5F4F0` |
| `--bg2` | `#ECEAE5` |
| `--white` | `#FFFFFF` |
| `--dark` | `#0F0F0F` |
| `--dark2` | `#1C1C1C` |

### Texto

| Token | Valor |
|-------|-------|
| `--text` | `#111111` |
| `--text2` | `#333333` |
| `--muted` | `#6B6B6B` |
| `--muted2` | `#9E9E9E` |

### Bordas

| Token | Valor |
|-------|-------|
| `--border` | `rgba(0, 0, 0, 0.08)` |
| `--border2` | `rgba(0, 0, 0, 0.14)` |
| `--border3` | `rgba(0, 0, 0, 0.24)` |

### Tipografia

| Token | Valor |
|-------|-------|
| `--font-title` | `'Roboto'` — títulos, labels, nav |
| `--font-body` | `'Inter'` — corpo, parágrafos |
| `--fw-light` | `300` |
| `--fw-regular` | `400` |
| `--fw-medium` | `500` |
| `--fw-semi` | `600` |
| `--fw-bold` | `700` |
| `--fw-black` | `900` |

### Escala tipográfica

| Token | Valor |
|-------|-------|
| `--text-xs` | `11px` |
| `--text-sm` | `12px` |
| `--text-base` | `14px` |
| `--text-md` | `15px` |
| `--text-lg` | `17px` |
| `--text-xl` | `20px` |
| `--text-2xl` | `clamp(20px, 2.2vw, 26px)` |
| `--text-3xl` | `clamp(26px, 3.2vw, 40px)` |
| `--text-hero` | `clamp(36px, 5vw, 58px)` |

### Border radius

| Token | Valor |
|-------|-------|
| `--r-xs` | `6px` |
| `--r-sm` | `10px` |
| `--r` | `14px` |
| `--r-lg` | `20px` |
| `--r-xl` | `28px` |

### Layout

| Token | Valor |
|-------|-------|
| `--maxw` | `1320px` |
| `--nav-h` | `62px` |

---

## 📄 Páginas — Estrutura de Seções

### `index.html` — Home

| Seção | Título |
|-------|--------|
| Hero | Desenvolvedor Full Stack Sênior |
| Tech strip | PHP · Joomla · Docker · React Native · MySQL |
| `section--white` | Destaques & Atuação |
| `section--alt` | Projetos Isolados |
| `section--white` | Stack & Proficiência |
| `section--alt` | Stack Tecnológica |
| `section--white` | Ferramentas & Ambiente |
| `section--alt` | Engenharia & Práticas |
| `section--white` | Dev & Versos |
| Contato | Pronto para o próximo desafio |

### `html/projects.html` — Cases & Atuação

| Seção | Título |
|-------|--------|
| `section--white` | Resumo do Portfólio |
| `section--alt` | Atuação, Ecossistemas & Stack |
| `section--white` | Projetos Isolados |
| `section--alt` | Experiência Corporativa |
| `section--white` | Mais Informações |

### `html/resume.html` — Currículo

| Seção | Título |
|-------|--------|
| Hero | Hirlei Carlos Pereira de Araújo |
| `section--white` | Resumo Profissional |
| `section--alt` | Resumo de Experiência |
| `section--white` | Experiência Profissional |
| `section--alt` | Formação & Habilidades |
| `section--white` | Cursos / Conhecimentos |

### `html/articles.html` — Artigos

| Seção | Título |
|-------|--------|
| `section--alt` | Dev & Versos (newsletter) |
| `section--white` | Artigos publicados |
| `section--alt` | Sobre a Dev & Versos |

### `html/sistemaocb.html` — Sistema OCB

| Seção | Título |
|-------|--------|
| `section--white` | O Ecossistema |
| `section--alt` | Núcleo do Ecossistema |
| `section--white` | Portais Estaduais |

### `html/cmsjoomla.html` — Engenharia Joomla

| Seção | Título |
|-------|--------|
| `section--white` | Engenharia Joomla |
| `section--alt` | Como eu organizo extensões |
| `section--white` | Open Source |
| `section--alt` | Projetos Corporativos (NDA) |
| `section--white` | Direção técnica |

### `html/ufg.html` — UFG

| Seção | Título |
|-------|--------|
| `section--white` | O Ecossistema UFG |
| `section--alt` | Stack e frentes de atuação |
| `section--white` | Capacidades e entregas |
| `section--alt` | Sites e sistemas |
| `section--white` | Portais Temáticos |

---

## 🏗 Arquitetura CSS — subpage.css

Grids disponíveis para as subpáginas:

| Classe | Colunas | Usado em |
|--------|---------|----------|
| `.proj-grid` | 3 colunas | sistemaocb, cmsjoomla |
| `.proj-grid--2` | 2 colunas | ufg — seção Stack |
| `.proj-grid--4` | 4 colunas | ufg — demais seções |
| `.states-grid` | 4 colunas | sistemaocb — portais estaduais |
| `.summary-stats` | 4 colunas | todas as subpáginas |

---

## 🖨 Sistema de PDF — Classes `pdfN`

O script lê `html/resume.html`, extrai os blocos marcados com `pdfN` e os injeta — ordenados numericamente — no template de impressão.

| Classe | Bloco extraído |
|--------|---------------|
| `pdf1` | `<header class="page-hero">` — nome, contato, título |
| `pdf2` | Resumo Profissional |
| `pdf3` | Competências Técnicas (dentro do `two-col`) |
| `pdf4` | Experiência Profissional |
| `pdf5` | Formação Acadêmica, Técnica e Idiomas (dentro do `two-col`) |
| `pdf6` | Cursos / Conhecimentos |

```html
<header class="page-hero pdf1">...</header>
<section class="section pdf2">...</section>
<section class="section pdf4">...</section>
<div class="two-col-card pdf5">...</div>
<div class="two-col-card pdf3">...</div>
<section class="section pdf6">...</section>
```

> A ordem das classes no HTML não importa. O script ordena numericamente por `N`.

---

## 🔄 Fluxo de Geração do PDF

```
html/resume.html
      │
      ▼
build_cv.py — BeautifulSoup
  ├─ extrai <header class="page-hero"> inteiro
  └─ extrai todos os blocos com classe pdfN do <main>
      │
      ▼
Ordenação numérica: pdf1 → pdf2 → pdf3 → ... → pdf6
      │
      ▼
Injeção no template: automacao/cv/templates/cv-print.html
      │
      ▼
HTML intermediário salvo em: automacao/cv/templates/.tmp/cv-rendered.html
      │
      ▼
Renderização via WeasyPrint + cv-print.css
      │
      ▼
assets/file/Curriculo_Hirlei_Carlos_RH_YYYYMMDD_HHMM.pdf
      │ (se --latest)
      ▼
assets/file/Curriculo_Hirlei_Carlos_RH.pdf  ← versão fixa atualizada
```

---

## ⚙️ Geração do PDF

### Requisitos

```bash
pip install weasyprint beautifulsoup4
```

- Python 3.10+
- WeasyPrint
- BeautifulSoup4

### Gerar com timestamp

```bash
python automacao/cv/scripts/build_cv.py
```

Saída: `assets/file/Curriculo_Hirlei_Carlos_RH_YYYYMMDD_HHMM.pdf`

### Gerar + atualizar versão fixa

```bash
python automacao/cv/scripts/build_cv.py --latest
```

Atualiza também: `assets/file/Curriculo_Hirlei_Carlos_RH.pdf`

### Parâmetros opcionais

| Parâmetro | Padrão | Descrição |
|-----------|--------|-----------|
| `--resume` | `html/resume.html` | Caminho do HTML fonte |
| `--template` | `automacao/cv/templates/cv-print.html` | Template de impressão |
| `--css` | `automacao/cv/styles/cv-print.css` | CSS de impressão |
| `--outdir` | `assets/file/` | Diretório de saída |
| `--prefix` | `Curriculo_Hirlei_Carlos_RH` | Prefixo do nome do arquivo |
| `--latest` | `False` | Atualiza também o arquivo fixo |

---

## 🔌 Extensões Joomla Open Source

Repositórios públicos com update server via XML em `updates/`:

| Extensão | Tipo | Repositório |
|----------|------|-------------|
| HC Mídias Sociais | Módulo Joomla 4/5/6 | [mod_hc_socialmedia](https://github.com/hirleicarlos/mod_hc_socialmedia) |
| Botão WhatsApp | Plugin System Joomla | [plg_system_btnwhatsapp](https://github.com/hirleicarlos/plg_system_btnwhatsapp) |
| HC Image Optimizer | Pacote Joomla 5/6 | [hc-image-optimizer](https://github.com/hirleicarlos/hc-image-optimizer) |
| HC Image Optimizer Media Action | Plugin Media Action Joomla 5/6 | [hc-image-optimizer](https://github.com/hirleicarlos/hc-image-optimizer) |

---

## 🌐 Open Graph / Social Meta

Todas as páginas têm meta tags completas para redes sociais:

- `og:type`, `og:url`, `og:site_name`, `og:locale` (pt_BR)
- `og:title`, `og:description`
- `og:image` → `assets/img/social.png` (1200×630)
- `twitter:card` → `summary_large_image`
- `apple-touch-icon`
- `favicon.ico` + `icon_hirlei.svg`

---

## 🚀 Hospedagem

```
https://hirleicarlos.github.io
```

Push para `main` → deploy automático via GitHub Pages.

---

## 🧾 Princípios de Engenharia

| Princípio | Aplicação |
|-----------|-----------|
| Separação Web × Impressão | Layout Web não interfere no PDF |
| Fonte única de verdade | Todo conteúdo do PDF vem de `resume.html` |
| Ordenação semântica | Classes `pdfN` controlam ordem no PDF |
| CSS de impressão isolado | `cv-print.css` sem conflitos com o site |
| Versionamento automático | PDF gerado com data/hora em America/Sao_Paulo |
| Design system compartilhado | `variaveis.css` alimenta todos os arquivos CSS |
| CSS por escopo | Cada página tem seu CSS específico |
| Modificadores de grid | `.proj-grid`, `.proj-grid--2`, `.proj-grid--4` |

---

## 📬 Contato

- 🌐 Site: [hirleicarlos.github.io](https://hirleicarlos.github.io)
- 💼 LinkedIn: [linkedin.com/in/hirleicarlos](https://linkedin.com/in/hirleicarlos)
- 🐙 GitHub: [github.com/hirleicarlos](https://github.com/hirleicarlos)
- ✉ E-mail: prof.hirleicarlos@gmail.com

---

© 2026 — Hirlei Carlos  
Desenvolvedor Full Stack Sênior | PHP & Joomla | Sistemas Corporativos | Governo e Educação
