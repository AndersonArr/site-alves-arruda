# Site do Alves & Arruda Advogados

Site estático publicado em www.alvesarruda.com.br (GitHub Pages).

## Como alterar
- Textos, contatos e áreas: `tools/conteudo.py`. Depois rode `cd tools && python3 gerar_paginas.py`.
- Estrutura das páginas: `tools/gerar_paginas.py`.
- Visual: `assets/css/site.css`.
- Fotos: coloque os originais em `fontes/` e rode `python3 tools/otimizar_imagens.py`.

## Verificação
`node tests/verificar.js` confere rolagem no celular, imagens, links, WhatsApp e abreviações proibidas. Resultado esperado: `0 falhas`.

## Nova landing page
Crie uma função de página em `tools/gerar_paginas.py` (use `pagina_area` como modelo) e grave em `nome-da-pagina/index.html`. Inclua o endereço no `sitemap()`.
