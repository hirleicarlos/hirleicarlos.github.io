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
- 📄 Currículo online (HTML) com sistema de geração de PDF
- 🖨 Sistema automatizado de geração de PDF via Python + WeasyPrint
- 🧠 Motor de ordenação semântica via classes `pdfN`
- 🚀 Hospedagem via GitHub Pages

O projeto separa completamente:

- **Camada de apresentação Web**
- **Camada de impressão (PDF)**
- **Camada de processamento e geração**

---

## 🔄 Redesign 2026 — O que mudou

O site passou por um **redesign completo** em abril de 2026. Todas as páginas foram reescritas do zero com um novo design system, mantendo o sistema de geração de PDF inalterado.

### Design System

| Token | Valor |
|-------|-------|
| Fonte títulos | Roboto (700/900) |
| Fonte corpo | Inter (400/500/600) |
| Cor primária | `#C41E20` (vermelho) |
| Fundo | `#F5F4F0` (off-white) |
| Dark footer | `#0F0F0F` |
| Max-width | `1320px` |
| Nav height | `62px` |

### Páginas redesenhadas

| Arquivo | Descrição |
|---------|-----------|
| `index.html` | Home — hero com foto, tech strip, destaques, stack, artigos, contato |
| `html/projects.html` | Cases & Atuação — 5 seções com alternância branco/cinza |
| `html/resume.html` | Currículo — timeline vertical, stats, formação, cursos, PDF identifiers |
| `html/articles.html` | Artigos — grid 3 colunas, 5 artigos + newsletter |
| `html/sistemaocb.html` | Case Sistema OCB — ecossistema cooperativista completo |
| `html/cmsjoomla.html` | Case Joomla — extensões, open source, NDA |
| `html/ufg.html` | Case UFG — ecossistema universitário, 4 colunas |

### CSS — Arquitetura de folhas de estilo

| Arquivo | Escopo |
|---------|--------|
| `variaveis.css` | Tokens globais: cores, tipografia, espaçamentos, sombras |
| `global.css` | Reset, navbar, footer, botões, tags, seções |
| `home.css` | Exclusivo da home (hero, tech strip, highlights, contact grid) |
| `projects.css` | Exclusivo de Cases & Atuação |
| `resume.css` | Exclusivo do currículo (timeline, stats, two-col, PDF classes) |
| `articles.css` | Exclusivo da página de artigos |
| `subpage.css` | Compartilhado entre sistemaocb, cmsjoomla e ufg |

### Grids do subpage.css

| Classe | Colunas | Usado em |
|--------|---------|----------|
| `.proj-grid` | 3 colunas | sistemaocb, cmsjoomla |
| `.proj-grid--2` | 2 colunas | ufg — seção Stack |
| `.proj-grid--4` | 4 colunas | ufg — demais seções |
| `.states-grid` | 4 colunas | sistemaocb — portais estaduais |
| `.summary-stats` | 4 colunas | todas as subpáginas |

---

## 🏗 Arquitetura do Sistema de PDF

```
┌─────────────────────────────┐
│   Camada de Apresentação    │
│   (HTML / CSS - Web)        │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│   Camada de Processamento   │
│   (Python + BeautifulSoup)  │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│   Template de Impressão     │
│   (HTML isolado para PDF)   │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│   Motor de Renderização     │
│       (WeasyPrint)          │
└─────────────────────────────┘
```

---

## 📁 Estrutura do Projeto

```
hirleicarlos.github.io/
│
├── index.html                          ← Home
├── gerar-cv.bat                        ← Atalho Windows para gerar PDF
│
├── html/
│   ├── resume.html                     ← Currículo (fonte do PDF)
│   ├── projects.html                   ← Cases & Atuação
│   ├── articles.html                   ← Artigos & Newsletter
│   ├── sistemaocb.html                 ← Case: Sistema OCB
│   ├── cmsjoomla.html                  ← Case: Engenharia Joomla
│   └── ufg.html                        ← Case: UFG
│
├── assets/
│   ├── css/
│   │   ├── variaveis.css               ← Tokens globais
│   │   ├── global.css                  ← Componentes globais
│   │   ├── home.css                    ← Estilos da home
│   │   ├── projects.css                ← Estilos de cases
│   │   ├── resume.css                  ← Estilos do currículo
│   │   ├── articles.css                ← Estilos de artigos
│   │   └── subpage.css                 ← Estilos das subpáginas
│   ├── js/
│   │   ├── nav.js                      ← Navbar responsiva
│   │   ├── main.js
│   │   └── masonry.js
│   ├── img/
│   │   ├── site/                       ← favicon, logo, icon SVG
│   │   ├── case/                       ← imagens dos projetos (.webp)
│   │   ├── artigos/                    ← capas Dev & Versos (.png)
│   │   └── hirlei.jpg                  ← foto do perfil
│   └── file/
│       └── Curriculo_Hirlei_Carlos_RH.pdf
│
└── automacao/
    └── cv/
        ├── scripts/
        │   └── build_cv.py             ← Script de geração do PDF
        ├── templates/
        │   └── cv-print.html           ← Template de impressão
        └── styles/
            └── cv-print.css            ← CSS específico para PDF
```

---

## 📄 Sistema de PDF — Classes `pdfN`

O currículo `html/resume.html` usa classes `pdfN` para controlar quais blocos são extraídos e em que ordem aparecem no PDF:

| Classe | Seção |
|--------|-------|
| `pdf1` | Cabeçalho — nome, contato, título |
| `pdf2` | Resumo Profissional |
| `pdf3` | Competências Técnicas |
| `pdf4` | Experiência Profissional |
| `pdf5` | Formação Acadêmica, Técnica e Idiomas |
| `pdf6` | Cursos / Conhecimentos |

```html
<header class="page-hero pdf1">...</header>
<section class="section pdf2">...</section>
<div class="two-col-card pdf3">...</div>
<section class="section pdf4">...</section>
```

O script Python identifica apenas blocos com `pdfN`, ordena numericamente e injeta no template de impressão. O layout Web permanece intacto.

---

## 🔄 Fluxo de Geração do PDF

```
resume.html
     │
     ▼
Extração dos blocos com classe pdfN
     │
     ▼
Ordenação numérica (pdf1 → pdf2 → ... → pdf6)
     │
     ▼
Injeção no template cv-print.html
     │
     ▼
Aplicação do cv-print.css
     │
     ▼
Renderização via WeasyPrint
     │
     ▼
Geração do PDF versionado
```

---

## 🖨 Geração Automatizada do PDF

### Requisitos

- Python 3.10+
- WeasyPrint
- BeautifulSoup4

### Instalação

```bash
pip install weasyprint beautifulsoup4
```

### Gerar PDF com timestamp

```bash
python automacao/cv/scripts/build_cv.py
```

Saída: `assets/file/Curriculo_Hirlei_Carlos_RH_YYYYMMDD_HHMM.pdf`

### Gerar + atualizar versão fixa

```bash
python automacao/cv/scripts/build_cv.py --latest
```

Também atualiza: `assets/file/Curriculo_Hirlei_Carlos_RH.pdf`

### Windows (atalho)

```
gerar-cv.bat
```

---

## 🎯 Princípios de Engenharia Aplicados

| Princípio | Aplicação |
|-----------|-----------|
| Separação Web × Impressão | Layout Web não interfere no PDF |
| Fonte única de verdade | Todo conteúdo vem de `resume.html` |
| Ordenação semântica | Controlada via classes `pdfN` |
| CSS de impressão isolado | `cv-print.css` sem conflitos com o site |
| Versionamento automatizado | Arquivos PDF gerados com data/hora |
| Design system compartilhado | `variaveis.css` alimenta todos os CSSs |
| CSS por escopo | Cada página tem seu CSS específico |

---

## 🧾 Estratégia de CSS para Impressão

O arquivo `automacao/cv/styles/cv-print.css` realiza:

- Remoção de navegação e footer
- Neutralização de grids e layouts responsivos
- Controle tipográfico para A4
- Controle de quebras de página entre seções
- Otimização para formato A4

---

## 🧠 Decisões Técnicas

| Decisão | Justificativa |
|---------|---------------|
| BeautifulSoup | Parsing HTML robusto e confiável |
| WeasyPrint | Renderização baseada em CSS real, suporta print media |
| Classes `pdfN` | Controle semântico, escalável e não invasivo |
| Template isolado | Separação clara entre layout web e PDF |
| CSS específico para print | Controle total de quebra de página |
| Subpage.css compartilhado | DRY entre sistemaocb, cmsjoomla e ufg |
| Grids por modificador | `.proj-grid`, `.proj-grid--2`, `.proj-grid--4` |

---

## 🚀 Hospedagem

Site hospedado via GitHub Pages:

```
https://hirleicarlos.github.io
```

Push para `main` → deploy automático.

---

## 📌 Tecnologias Utilizadas

- HTML5 semântico com `aria-*` e roles de acessibilidade
- CSS3 — Grid, Custom Properties (variáveis), Flexbox
- Python 3.10+ — BeautifulSoup4, WeasyPrint
- GitHub Pages

---

## 📈 Roadmap

- [ ] Pipeline CI para geração automática de PDF no push
- [ ] Dockerização do motor de geração
- [ ] Dark mode
- [ ] Exportação estruturada (JSON)
- [ ] Analytics

---

## 📬 Contato

- 🌐 Site: https://hirleicarlos.github.io
- 💼 LinkedIn: https://linkedin.com/in/hirleicarlos
- 🐙 GitHub: https://github.com/hirleicarlos
- ✉ E-mail: prof.hirleicarlos@gmail.com

---

© 2026 — Hirlei Carlos
Desenvolvedor Full Stack Sênior | PHP & Joomla | Sistemas Corporativos | Governo e Educação