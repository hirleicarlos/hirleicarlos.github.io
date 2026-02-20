# 👨‍💻 Hirlei Carlos — Portfólio Profissional & Sistema Automatizado de Currículo

![Status](https://img.shields.io/badge/status-ativo-success)
![Stack](https://img.shields.io/badge/stack-HTML%20%7C%20CSS%20%7C%20Python-blue)
![PDF Engine](https://img.shields.io/badge/PDF-WeasyPrint-orange)
![Hospedagem](https://img.shields.io/badge/hosting-GitHub%20Pages-black)

---

## 📌 Visão Geral

Este repositório contém:

- 🌐 Site profissional estático
- 📄 Currículo online (HTML)
- 🖨 Sistema automatizado de geração de PDF
- 🧠 Motor de ordenação semântica via classes `pdfN`
- 🚀 Hospedagem via GitHub Pages

O projeto separa completamente:

- **Camada de apresentação Web**
- **Camada de impressão (PDF)**
- **Camada de processamento e geração**

Garantindo organização, escalabilidade e manutenção simplificada.

---

# 🏗 Arquitetura do Sistema

O sistema foi projetado em camadas independentes:

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

# 📁 Estrutura do Projeto

```
hirleicarlos.github.io/
│
├── index.html
├── html/
│   ├── resume.html
│   └── projects.html
│
├── assets/
│   ├── css/
│   ├── img/
│   └── file/
│
└── automacao/
    └── cv/
        ├── scripts/
        │   └── build_cv.py
        ├── templates/
        │   └── cv-print.html
        └── styles/
            └── cv-print.css
```

---

# 📄 Lógica de Estrutura do Currículo (Sistema `pdfN`)

O arquivo principal do currículo é:

```
html/resume.html
```

Os blocos que devem aparecer no PDF recebem classes no formato:

```html
<section class="section pdf2">...</section>
<div class="card pdf3">...</div>
<section class="section pdf4">...</section>
```

## 🔎 Funcionamento

- `pdfN` define a prioridade de renderização.
- O script Python identifica apenas blocos com `pdfN`.
- Os blocos são ordenados numericamente.
- Apenas esses blocos são inseridos no template de impressão.
- O layout Web permanece intacto.

Essa estratégia permite:

- Separação de responsabilidades
- Controle total da ordem
- Manutenção simples
- Zero duplicação de conteúdo

---

# 🔄 Fluxo de Geração do PDF

```
resume.html
     │
     ▼
Extração do <header.hero>
Extração do <main#conteudo>
     │
     ▼
Identificação dos blocos com classe pdfN
     │
     ▼
Ordenação numérica dos blocos
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

# 🖨 Geração Automatizada do PDF

## Requisitos

- Python 3.10+
- WeasyPrint
- BeautifulSoup

## Instalação das Dependências

```bash
pip install weasyprint beautifulsoup4
```

## Gerar PDF com versão timestamp

```bash
python automacao/cv/scripts/build_cv.py
```

Saída:

```
assets/file/Curriculo_Hirlei_Carlos_RH_YYYYMMDD_HHMM.pdf
```

## Atualizar versão fixa

```bash
python automacao/cv/scripts/build_cv.py --latest
```

Também atualiza:

```
assets/file/Curriculo_Hirlei_Carlos_RH.pdf
```

---

# 🎯 Princípios de Engenharia Aplicados

### ✅ Separação Web x Impressão
Layout Web não interfere no layout do PDF.

### ✅ Fonte Única de Verdade
Todo conteúdo vem de `resume.html`.

### ✅ Ordenação Baseada em Semântica
A lógica de estrutura é controlada via classes CSS.

### ✅ CSS de Impressão Isolado
Estilo específico para PDF evita conflitos.

### ✅ Versionamento Automatizado
Arquivos gerados com data/hora.

### ✅ Manutenção Simplificada
Cada responsabilidade está isolada:
- HTML Web
- Template PDF
- CSS de Impressão
- Script Python

---

# 🧠 Decisões Técnicas

| Decisão | Justificativa |
|----------|---------------|
| BeautifulSoup | Parsing HTML robusto |
| WeasyPrint | Renderização baseada em CSS real |
| Classes pdfN | Controle semântico e escalável |
| Template isolado | Separação clara de layout |
| CSS específico para print | Controle total de quebra de página |

---

# 🧾 Estratégia de CSS para Impressão

O arquivo:

```
automacao/cv/styles/cv-print.css
```

Realiza:

- Remoção de navegação
- Neutralização de grids
- Controle tipográfico
- Controle de quebras de página
- Otimização para formato A4

---

# 🚀 Hospedagem

Site hospedado via GitHub Pages:

```
https://hirleicarlos.github.io
```

---

# 📌 Tecnologias Utilizadas

- HTML5
- CSS3
- Python 3.10+
- WeasyPrint
- BeautifulSoup
- GitHub Pages

---

# 📈 Roadmap Futuro

- Pipeline CI para geração automática de PDF
- Dockerização do motor de geração
- Suporte multilíngue
- Versão dark-mode do portfólio
- Exportação estruturada (JSON)
- Métricas e analytics

---

# 📬 Contato

- LinkedIn: https://linkedin.com/in/hirleicarlos
- GitHub: https://github.com/hirleicarlos
- Site: https://hirleicarlos.github.io

---

© 2026 — Hirlei Carlos  
Desenvolvedor Web Sênior | PHP & Joomla | Sistemas Corporativos | Governo e Educação