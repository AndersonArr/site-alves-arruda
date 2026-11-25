# Site institucional Alves & Arruda: plano de execução

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Site estático publicado em www.alvesarruda.com.br, com página principal, 5 (cinco) páginas de área, privacidade e 404.

**Architecture:** HTML, CSS e JavaScript puros, sem compilação. Um `assets/css/site.css` e um `assets/js/site.js` compartilhados; cabeçalho e rodapé repetidos em cada página (HTML estático, melhor para o Google). Hospedagem no GitHub Pages com arquivo `CNAME`.

**Tech Stack:** HTML5, CSS (variáveis, grid), JavaScript sem bibliotecas, Google Fonts (Playfair Display, DM Sans), Python com Pillow para otimizar imagens, Playwright para testes.

**Spec:** `docs/superpowers/specs/2026-11-25-site-institucional-design.md`

## Global Constraints

- Cores: #322620, #FFB980, #DCA06F, #F6E9DA, #6B5244, #FBF6EF. Dourado #FFB980 nunca como texto sobre fundo claro.
- Fontes: Playfair Display (títulos, itálico nos destaques) e DM Sans (corpo). Nada além.
- Texto sem abreviações (proibido: "Av.", "Ed.", "nº", "art.", "CF", "CPC", "Dr." no corpo). Exceção: "OAB/GO 37.973" e "OAB/GO 38.689".
- Números em algarismo com extenso entre parênteses, exceto anos, datas, telefones, CEP e números de inscrição.
- Contatos: WhatsApp 5562985109393 (Anderson) e 5562982624401 (Roberta); e-mail alvesarrudaadvogados@gmail.com; Avenida E, número 1470, sala 608, Edifício JK New Concept, Jardim Goiás, Goiânia, Goiás, CEP 74810-030; segunda a sexta, das 8h às 18h; Instagram @andersonarrudaadvogado e @robertaalvesadvogada.
- Sem promessa de resultado, sem honorários, sem contagem de processos.
- Animações respeitam `prefers-reduced-motion`.

## Review Focus

1. Celular de 360 pixels de largura: nenhuma rolagem horizontal, menu abre e fecha.
2. Imagens quebradas ou pesadas: toda imagem existe e nenhuma passa de 400 KB.
3. Links do WhatsApp e âncoras do menu levam ao lugar certo em todas as páginas.
4. Abreviações proibidas escapando nos textos.
5. Leitura do título sobre a foto da fachada (contraste da película).

---

### Task 1: Imagens

**Files:** Create `assets/img/*.webp` e `*.jpg`, `tools/otimizar_imagens.py`

- [ ] Baixar as 15 (quinze) fotos da pasta do Drive para `fontes/` (fora do site, ignorada no git).
- [ ] `tools/otimizar_imagens.py`: redimensiona para no máximo 2000 pixels (abertura) e 1200 pixels (demais), grava `.webp` qualidade 78 e `.jpg` de reserva.
- [ ] Verificar: `ls -la assets/img`, nenhum arquivo maior que 400 KB.
- [ ] Commit.

### Task 2: Página principal

**Files:** Create `index.html`, `assets/css/site.css`, `assets/js/site.js`

- [ ] Seções na ordem da seção 6 do projeto, com âncoras `#sobre`, `#atuacao`, `#socios`, `#espaco`, `#contato`.
- [ ] `site.js`: menu móvel (`.nav-toggle` alterna `body.menu-aberto`), cabeçalho muda ao rolar (`.rolado`), surgimento ao rolar via IntersectionObserver na classe `.revelar`.
- [ ] Commit.

### Task 3: Páginas internas

**Files:** Create `familia/index.html`, `direito-medico/index.html`, `saude-autismo-inclusao/index.html`, `civil-consumidor/index.html`, `empresarial/index.html`, `privacidade/index.html`, `404.html`

- [ ] Mesmo cabeçalho e rodapé; abertura curta, texto da área, "Situações em que podemos ajudar", chamada para o WhatsApp com mensagem pronta da área.
- [ ] Commit.

### Task 4: Google e publicação

**Files:** Create `CNAME` (`www.alvesarruda.com.br`), `robots.txt`, `sitemap.xml`, `assets/img/compartilhar.jpg` (1200x630), favicon a partir de `simbolo.png`; dados estruturados `LegalService` no `index.html`.

- [ ] Commit.

### Task 5: Testes

**Files:** Create `tests/verificar.js`

- [ ] Para cada página, em 360 e 1366 pixels: `scrollWidth <= innerWidth`; todas as imagens com `naturalWidth > 0`; todo link interno responde 200; links `wa.me` usam um dos 2 (dois) números; texto visível não contém as abreviações proibidas.
- [ ] Executar `node tests/verificar.js` com servidor local; esperado: "0 falhas".
- [ ] Capturas de tela para a prévia; commit.
