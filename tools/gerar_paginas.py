"""Gera todas as páginas HTML do site a partir de tools/conteudo.py.
Uso: python3 tools/gerar_paginas.py"""
import json
from html import escape
from pathlib import Path
from urllib.parse import quote

import conteudo as c

RAIZ = Path(__file__).resolve().parent.parent
VERSAO = "20261125"

SETA = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><path d="M7 17 17 7M8 7h9v9"/></svg>'
SETA_BAIXO = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><path d="M12 5v14M6 13l6 6 6-6"/></svg>'
WHATS_SVG = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12.04 2C6.58 2 2.13 6.45 2.13 11.91c0 1.75.46 3.45 1.32 4.95L2.05 22l5.25-1.38a9.9 9.9 0 0 0 4.74 1.21h.01c5.46 0 9.91-4.45 9.91-9.91A9.85 9.85 0 0 0 12.04 2Zm0 18.15h-.01a8.23 8.23 0 0 1-4.2-1.15l-.3-.18-3.12.82.83-3.04-.2-.31a8.2 8.2 0 0 1-1.26-4.38c0-4.54 3.7-8.23 8.25-8.23a8.2 8.2 0 0 1 8.23 8.24c0 4.54-3.7 8.23-8.22 8.23Zm4.52-6.16c-.25-.12-1.47-.72-1.69-.81-.23-.08-.39-.12-.56.13-.16.25-.64.81-.79.97-.14.17-.29.19-.54.06-.25-.12-1.05-.39-1.99-1.23-.74-.66-1.23-1.47-1.38-1.72-.14-.25-.02-.38.11-.51.11-.11.25-.29.37-.43.12-.15.16-.25.25-.42.08-.17.04-.31-.02-.43-.06-.13-.56-1.35-.77-1.84-.2-.48-.41-.42-.56-.43h-.48a.92.92 0 0 0-.66.31c-.23.25-.87.85-.87 2.07 0 1.22.89 2.4 1.01 2.56.12.17 1.75 2.67 4.24 3.74.59.26 1.05.41 1.41.52.59.19 1.13.16 1.56.1.48-.07 1.47-.6 1.67-1.18.21-.58.21-1.07.14-1.18-.06-.1-.22-.16-.47-.29Z"/></svg>'


def whats(numero: str, mensagem: str = "Olá! Gostaria de falar com o escritório Alves & Arruda Advogados.") -> str:
    return f"https://wa.me/{numero}?text={quote(mensagem)}"


def icone(nome: str, classe: str = "area-icone") -> str:
    return f'<svg class="{classe}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{c.ICONES[nome]}</svg>'


def foto(r: str, nome: str, alt: str, largura: int, altura: int, lazy: bool = True, extra: str = "") -> str:
    carregar = 'loading="lazy" decoding="async"' if lazy else 'fetchpriority="high"'
    return f'<img src="{r}assets/img/{nome}.webp" alt="{escape(alt)}" width="{largura}" height="{altura}" {carregar}{extra}>'


def cabecalho(r: str, inicio: bool) -> str:
    ancora = "#" if inicio else f"{r}#"
    solido = "" if inicio else " solido"
    return f"""<a class="pular" href="#conteudo">Ir para o conteúdo</a>
<header class="cabecalho{solido}">
  <div class="conteiner">
    <a class="marca" href="{r or './'}" aria-label="{c.NOME}, página inicial"><img src="{r}assets/logo/logo-dourada.png" alt="{c.NOME}" width="744" height="354"></a>
    <button class="alternar-menu" type="button" aria-label="Abrir menu" aria-expanded="false" aria-controls="menu"><span></span><span></span><span></span></button>
    <nav class="menu" id="menu" aria-label="Menu principal">
      <a href="{ancora}sobre">O escritório</a>
      <a href="{ancora}atuacao">Atuação</a>
      <a href="{ancora}socios">Sócios</a>
      <a href="{ancora}contato">Contato</a>
      <a class="botao botao-principal" href="{whats(c.WHATS_ANDERSON)}" target="_blank" rel="noopener">Fale conosco {SETA}</a>
    </nav>
  </div>
</header>"""


def rodape(r: str) -> str:
    areas = "\n".join(f'<li><a href="{r}{a["slug"]}/">{a["titulo"]}</a></li>' for a in c.AREAS)
    endereco = "<br>".join(c.ENDERECO_LINHAS)
    return f"""<footer class="rodape">
  <div class="conteiner">
    <div class="rodape-grade">
      <div>
        <img src="{r}assets/logo/logo-dourada.png" alt="{c.NOME}" width="744" height="354" loading="lazy">
        <p>Estratégia jurídica para proteger o que importa.</p>
      </div>
      <div><h4>Atuação</h4><ul>{areas}</ul></div>
      <div><h4>Escritório</h4><ul>
        <li><a href="{r}#sobre">O escritório</a></li>
        <li><a href="{r}#socios">Sócios</a></li>
        <li><a href="{r}#espaco">Nosso espaço</a></li>
        <li><a href="{r}privacidade/">Política de privacidade</a></li>
      </ul></div>
      <div><h4>Contato</h4><ul>
        <li><a href="{whats(c.WHATS_ANDERSON)}" target="_blank" rel="noopener">{c.TELEFONE_ANDERSON}</a></li>
        <li><a href="{whats(c.WHATS_ROBERTA)}" target="_blank" rel="noopener">{c.TELEFONE_ROBERTA}</a></li>
        <li><a href="mailto:{c.EMAIL}">{c.EMAIL}</a></li>
        <li>{endereco}</li>
      </ul></div>
    </div>
    <div class="rodape-base">
      <span>© <span data-ano>2026</span> {c.NOME}. Anderson Arruda, OAB/GO 37.973. Roberta Alves, OAB/GO 38.689.</span>
      <a href="{r}privacidade/">Privacidade</a>
    </div>
  </div>
</footer>
<a class="whatsapp-flutuante" href="{whats(c.WHATS_ANDERSON)}" target="_blank" rel="noopener" aria-label="Conversar pelo WhatsApp">{WHATS_SVG}</a>"""


def documento(r: str, caminho: str, titulo: str, descricao: str, corpo: str, inicio: bool = False, extra_head: str = "") -> str:
    url = f"{c.DOMINIO}/{caminho}"
    return f"""<!doctype html>
<html lang="pt-BR" class="sem-js">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{escape(titulo)}</title>
<meta name="description" content="{escape(descricao)}">
<link rel="canonical" href="{url}">
<meta name="theme-color" content="#322620">
<meta property="og:type" content="website">
<meta property="og:locale" content="pt_BR">
<meta property="og:site_name" content="{c.NOME}">
<meta property="og:title" content="{escape(titulo)}">
<meta property="og:description" content="{escape(descricao)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{c.DOMINIO}/assets/img/compartilhar.jpg">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" type="image/png" sizes="32x32" href="{r}favicon-32.png">
<link rel="apple-touch-icon" href="{r}apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=DM+Sans:opsz,wght@9..40,400;9..40,500;9..40,600&family=Playfair+Display:ital,wght@0,400;0,500;1,400;1,500&display=swap">
<link rel="stylesheet" href="{r}assets/css/site.css?v={VERSAO}">
{extra_head}</head>
<body>
{cabecalho(r, inicio)}
<main id="conteudo">
{corpo}
</main>
{rodape(r)}
<script src="{r}assets/js/site.js?v={VERSAO}" defer></script>
</body>
</html>
"""


def dados_estruturados() -> str:
    dados = {
        "@context": "https://schema.org",
        "@type": "LegalService",
        "name": c.NOME,
        "url": c.DOMINIO + "/",
        "logo": c.DOMINIO + "/icone-512.png",
        "image": c.DOMINIO + "/assets/img/compartilhar.jpg",
        "email": c.EMAIL,
        "telephone": "+55 62 98510-9393",
        "address": {
            "@type": "PostalAddress",
            "streetAddress": "Avenida E, 1470, sala 608, Edifício JK New Concept",
            "addressLocality": "Goiânia",
            "addressRegion": "GO",
            "postalCode": "74810-030",
            "addressCountry": "BR",
        },
        "openingHoursSpecification": [{
            "@type": "OpeningHoursSpecification",
            "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
            "opens": "08:00", "closes": "18:00",
        }],
        "areaServed": "BR",
        "sameAs": [c.INSTAGRAM_ANDERSON, c.INSTAGRAM_ROBERTA],
        "employee": [
            {"@type": "Person", "name": "Anderson Augusto Arruda Pereira", "jobTitle": "Advogado"},
            {"@type": "Person", "name": "Roberta Alves da Silva", "jobTitle": "Advogada"},
        ],
    }
    return f'<script type="application/ld+json">{json.dumps(dados, ensure_ascii=False)}</script>\n'


def pagina_inicial() -> str:
    r = ""
    areas_cartoes = "\n".join(f"""      <a class="area revelar" href="{a['slug']}/">
        <span class="area-numero">0{i}</span>
        {icone(a['icone'])}
        <h3>{a['titulo']}</h3>
        <p>{a['resumo']}</p>
        <span class="link-seta">Saiba mais {SETA}</span>
      </a>""" for i, a in enumerate(c.AREAS, 1))
    faixa_itens = "".join(f"<span>{a['titulo']}</span>" for a in c.AREAS) + "<span>Atendimento presencial e online</span>"
    principios = "\n".join(f'<div class="principio revelar"><h3>{t}</h3><p>{d}</p></div>' for t, d in c.PRINCIPIOS)
    endereco = "<br>".join(c.ENDERECO_LINHAS)
    mapa = f"https://www.google.com/maps?q={quote(c.MAPA_BUSCA)}&output=embed"
    rota = f"https://www.google.com/maps/search/?api=1&query={quote(c.MAPA_BUSCA)}"
    corpo = f"""<section class="abertura" aria-label="Apresentação">
  <div class="abertura-foto">{foto(r, 'fachada', 'Fachada do Edifício JK New Concept, sede do escritório no Jardim Goiás', 481, 440, lazy=False)}</div>
  <div class="abertura-conteudo">
    <div class="conteiner">
      <p class="rotulo">Proximidade. Clareza. Estratégia.</p>
      <h1>Estratégia jurídica para proteger <em>o que importa.</em></h1>
      <p class="lead">Pessoas, famílias e negócios. Uma advocacia que compreende a sua realidade para construir o próximo passo.</p>
      <div class="abertura-botoes">
        <a class="botao botao-principal" href="{whats(c.WHATS_ANDERSON)}" target="_blank" rel="noopener">{WHATS_SVG} Converse com o escritório</a>
        <a class="botao botao-contorno" href="#atuacao">Conheça nossa atuação {SETA_BAIXO}</a>
      </div>
      <p class="abertura-nota">Atendimento presencial em Goiânia e online em todo o Brasil</p>
    </div>
  </div>
  <div class="destaques">
    <div class="conteiner">
      <div class="destaque"><strong>Desde 2013</strong><span>Advocacia em Goiânia</span></div>
      <div class="destaque"><strong>5 (cinco) áreas</strong><span>Atuação complementar</span></div>
      <div class="destaque"><strong>Todo o Brasil</strong><span>Atendimento online</span></div>
    </div>
  </div>
</section>

<div class="faixa" aria-hidden="true"><div class="faixa-trilho">{faixa_itens}{faixa_itens}</div></div>

<section class="secao" id="sobre">
  <div class="conteiner duas-colunas">
    <div class="revelar">
      <div class="foto-moldura">{foto(r, 'socios-trabalhando', 'Anderson Arruda e Roberta Alves analisando documentos no escritório', 1600, 1059)}</div>
      <p class="foto-legenda">Anderson Arruda e Roberta Alves</p>
    </div>
    <div class="revelar">
      <p class="rotulo">O escritório</p>
      <h2 class="titulo-secao">Mais do que conhecer a lei, é preciso compreender <em>o que está em jogo.</em></h2>
      <hr class="filete">
      <p class="citacao">Cada cliente traz uma história. Nosso trabalho começa pela escuta.</p>
      <p>Uma família em reorganização. Uma criança que precisa de tratamento ou de inclusão adequada. Um patrimônio construído durante anos. Uma empresa que precisa reduzir riscos.</p>
      <p>O Alves & Arruda Advogados reúne a experiência de Anderson Arruda e Roberta Alves em uma atuação técnica e próxima. Compreendemos o contexto de cada cliente para construir estratégias individualizadas, com comunicação direta e linguagem clara.</p>
      <a class="link-seta" href="#socios">Conheça os sócios {SETA}</a>
    </div>
  </div>
</section>

<section class="secao areia" id="atuacao">
  <div class="conteiner">
    <div class="cabeca-secao revelar">
      <div>
        <p class="rotulo">Áreas de atuação</p>
        <h2 class="titulo-secao">Diferentes necessidades. <em>A mesma atenção.</em></h2>
      </div>
      <p class="lead">Experiências complementares para orientar decisões e proteger interesses em momentos importantes.</p>
    </div>
    <div class="areas">
{areas_cartoes}
    </div>
  </div>
</section>

<section class="destaque-area escuro" aria-label="Direito Médico e da Saúde">
  <div class="destaque-area-foto">{foto(r, 'roberta-trabalhando', 'Roberta Alves trabalhando no escritório', 846, 1280)}</div>
  <div class="destaque-area-texto revelar">
    <p class="rotulo">Direito Médico e da Saúde</p>
    <h2>Segurança jurídica para quem cuida <em>de outras pessoas.</em></h2>
    <p class="lead">Assessoria a profissionais e clínicas para organizar documentos, reduzir vulnerabilidades e oferecer suporte na prevenção e na solução de conflitos.</p>
    <p><a class="botao botao-principal" href="direito-medico/">Conheça essa atuação {SETA}</a></p>
  </div>
</section>

<section class="secao">
  <div class="conteiner">
    <div class="revelar">
      <p class="rotulo">Nossa forma de trabalhar</p>
      <h2 class="titulo-secao">Técnica nas decisões. <em>Proximidade em cada etapa.</em></h2>
    </div>
    <div class="principios">
{principios}
    </div>
  </div>
</section>

<section class="secao escuro" id="socios">
  <div class="conteiner">
    <div class="cabeca-secao revelar">
      <div>
        <p class="rotulo">Os sócios</p>
        <h2 class="titulo-secao">Duas trajetórias. <em>Um compromisso em comum.</em></h2>
      </div>
      <p class="lead">Mais de uma década de experiência, unindo conhecimento jurídico, escuta atenta e dedicação para proteger o que importa para você.</p>
    </div>
    <div class="socios">
      <article class="socio revelar">
        <div class="socio-foto">{foto(r, 'anderson-retrato', 'Anderson Arruda, advogado e sócio', 1000, 1020)}</div>
        <p class="socio-inscricao">OAB/GO 37.973 · Advocacia desde 2013</p>
        <h3>Anderson Arruda</h3>
        <p>Pós-graduando em Planejamento Patrimonial e Sucessório. Graduado em Direito pela Universidade Salgado de Oliveira.</p>
        <p>Atuação voltada especialmente ao Direito de Família e Sucessões, ao Direito Civil e à assessoria jurídica empresarial, com análise estratégica, soluções individualizadas e comunicação clara.</p>
        <a class="link-seta" href="{c.INSTAGRAM_ANDERSON}" target="_blank" rel="noopener">Acompanhe no Instagram {SETA}</a>
      </article>
      <article class="socio revelar">
        <div class="socio-foto">{foto(r, 'roberta-retrato', 'Roberta Alves, advogada e sócia', 846, 1280)}</div>
        <p class="socio-inscricao">OAB/GO 38.689 · Advocacia desde 2013</p>
        <h3>Roberta Alves</h3>
        <p>Pós-graduada em Direito Médico e da Saúde. Graduada em Direito pela Universidade Salgado de Oliveira.</p>
        <p>Atuação voltada especialmente ao Direito à Saúde e ao Direito Médico, com atenção aos direitos de pessoas e famílias e à assessoria de profissionais e estabelecimentos de saúde.</p>
        <a class="link-seta" href="{c.INSTAGRAM_ROBERTA}" target="_blank" rel="noopener">Acompanhe no Instagram {SETA}</a>
      </article>
    </div>
  </div>
</section>

<section class="secao" id="espaco">
  <div class="conteiner">
    <div class="cabeca-secao revelar">
      <div>
        <p class="rotulo">Nosso espaço</p>
        <h2 class="titulo-secao">Um ambiente pensado <em>para receber você.</em></h2>
      </div>
      <p class="lead">Contato próximo também se constrói com espaço para conversar, compreender e planejar.</p>
    </div>
    <div class="galeria revelar">
      <figure>{foto(r, 'sala-convivencia', 'Sala de recepção do escritório, com sofá e poltronas', 1280, 960)}<figcaption>Recepção</figcaption></figure>
      <figure>{foto(r, 'espaco-atendimento', 'Sala de atendimento do escritório', 1280, 960)}<figcaption>Sala de atendimento</figcaption></figure>
      <figure>{foto(r, 'socios-poltrona', 'Roberta Alves e Anderson Arruda no escritório', 1000, 1558, extra=' style="object-position: center 25%"')}<figcaption>Os sócios</figcaption></figure>
      <figure>{foto(r, 'area-convivencia', 'Área de convivência do Edifício JK New Concept à noite', 694, 567)}<figcaption>Área de convivência do edifício</figcaption></figure>
    </div>
  </div>
</section>

<section class="secao escuro" id="contato">
  <div class="conteiner contato-grade">
    <div class="revelar">
      <p class="rotulo">Fale conosco</p>
      <h2 class="titulo-secao">Vamos conversar sobre <em>o que importa para você?</em></h2>
      <p class="lead">Entre em contato para informações e agendamento. Atendimento presencial em Goiânia e online em todo o Brasil.</p>
      <div class="contato-botoes">
        <a class="botao botao-principal" href="{whats(c.WHATS_ANDERSON)}" target="_blank" rel="noopener"><span>Anderson Arruda<small>WhatsApp {c.TELEFONE_ANDERSON}</small></span>{WHATS_SVG}</a>
        <a class="botao botao-contorno" href="{whats(c.WHATS_ROBERTA)}" target="_blank" rel="noopener"><span>Roberta Alves<small>WhatsApp {c.TELEFONE_ROBERTA}</small></span>{WHATS_SVG}</a>
      </div>
    </div>
    <div class="contato-dados revelar">
      <div class="contato-item"><h3>Visite o escritório</h3><p>{endereco}</p><p style="margin-top:10px"><a class="link-seta" href="{rota}" target="_blank" rel="noopener">Como chegar {SETA}</a></p></div>
      <div class="contato-item"><h3>Horário de atendimento</h3><p>{c.HORARIO}</p></div>
      <div class="contato-item"><h3>E-mail</h3><p><a href="mailto:{c.EMAIL}">{c.EMAIL}</a></p></div>
      <div class="mapa"><iframe src="{mapa}" title="Mapa com a localização do escritório" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe></div>
    </div>
  </div>
</section>"""
    return documento(r, "", f"{c.NOME} | Família, Saúde, Civil e Empresarial em Goiânia",
                     "Escritório de advocacia em Goiânia com atuação em Família e Sucessões, Direito Médico e da Saúde, Autismo e Inclusão, Direito Civil e do Consumidor e assessoria empresarial. Atendimento online em todo o Brasil.",
                     corpo, inicio=True, extra_head=dados_estruturados())


def pagina_area(area: dict) -> str:
    r = "../"
    como = "\n".join(f"<p>{p}</p>" for p in area["como"])
    situacoes = "\n".join(f"<li>{s}</li>" for s in area["situacoes"])
    outras = "\n".join(f'<a href="{r}{a["slug"]}/">{a["titulo"]}</a>' for a in c.AREAS if a["slug"] != area["slug"])
    link = whats(area["whats"], area["mensagem"])
    corpo = f"""<section class="abertura-interna">
  <div class="conteiner">
    <p class="trilha"><a href="{r}">Início</a> / <a href="{r}#atuacao">Áreas de atuação</a> / {area['titulo']}</p>
    <p class="rotulo">{area['titulo']}</p>
    <h1>{area['chamada_titulo']}</h1>
    <p class="lead">{area['resumo']}</p>
    <div class="abertura-botoes" style="margin-top:36px">
      <a class="botao botao-principal" href="{link}" target="_blank" rel="noopener">{WHATS_SVG} Converse com o escritório</a>
    </div>
  </div>
</section>

<section class="secao">
  <div class="conteiner texto-corrido">
    <h2>Como podemos ajudar</h2>
    <p class="lead">{area['introducao']}</p>
    <h2>Situações em que atuamos</h2>
    <ul class="lista-situacoes">
{situacoes}
    </ul>
    <h2>Como conduzimos o seu caso</h2>
{como}
    <p class="aviso">Cada caso tem particularidades. As informações desta página são gerais e não substituem a análise individual feita por um advogado.</p>
  </div>
</section>

<section class="secao areia chamada">
  <div class="conteiner">
    <p class="rotulo">Fale conosco</p>
    <h2>Vamos conversar sobre <em>a sua situação?</em></h2>
    <p class="lead">Conte brevemente o que está acontecendo. Retornamos para orientar sobre os próximos passos.</p>
    <a class="botao botao-escuro" href="{link}" target="_blank" rel="noopener">{WHATS_SVG} Conversar pelo WhatsApp</a>
    <div class="outras-areas" style="justify-content:center;margin-top:56px">{outras}</div>
  </div>
</section>"""
    titulo = f"{area['titulo']} em Goiânia | {c.NOME}"
    return documento(r, f"{area['slug']}/", titulo, area["resumo"], corpo)


def pagina_privacidade() -> str:
    r = "../"
    corpo = f"""<section class="abertura-interna">
  <div class="conteiner">
    <p class="trilha"><a href="{r}">Início</a> / Política de privacidade</p>
    <h1>Política de <em>privacidade</em></h1>
    <p class="lead">Como o {c.NOME} trata as informações de quem visita este site.</p>
  </div>
</section>
<section class="secao">
  <div class="conteiner texto-corrido">
    <h2>Quais dados coletamos</h2>
    <p>Este site não possui formulários e não pede cadastro. Não coletamos dados pessoais diretamente pelo site. Quando você clica em um botão do WhatsApp ou do e-mail, a conversa acontece nesses aplicativos, e os dados que você decidir compartilhar serão usados somente para responder ao seu contato e prestar o atendimento solicitado.</p>
    <h2>Serviços de terceiros</h2>
    <p>Para exibir o mapa e as fontes tipográficas, o site carrega recursos do Google (Google Maps e Google Fonts). Esses serviços podem registrar informações técnicas da sua visita, como o endereço de internet do seu aparelho, conforme as políticas de privacidade do próprio Google. O site é hospedado no GitHub Pages, que mantém registros técnicos de acesso para fins de segurança.</p>
    <h2>Sigilo profissional</h2>
    <p>Todas as informações compartilhadas com o escritório são tratadas com sigilo profissional, nos termos do Estatuto da Advocacia (Lei 8.906 de 1994) e da Lei Geral de Proteção de Dados Pessoais (Lei 13.709 de 2018).</p>
    <h2>Seus direitos</h2>
    <p>Você pode solicitar a confirmação, o acesso, a correção ou a exclusão dos seus dados pessoais tratados pelo escritório, nos termos do artigo 18 da Lei Geral de Proteção de Dados Pessoais. Para isso, escreva para <a href="mailto:{c.EMAIL}">{c.EMAIL}</a>.</p>
    <p class="aviso">Última atualização: 25 de novembro de 2026.</p>
  </div>
</section>"""
    return documento(r, "privacidade/", f"Política de privacidade | {c.NOME}",
                     "Como o Alves & Arruda Advogados trata as informações de quem visita o site.", corpo)


def pagina_404() -> str:
    r = "/"
    corpo = f"""<section class="abertura-interna" style="min-height:80vh;display:flex;align-items:center">
  <div class="conteiner">
    <p class="rotulo">Página não encontrada</p>
    <h1>Esta página <em>não existe ou mudou de endereço.</em></h1>
    <p class="lead">Volte para a página inicial ou fale diretamente com o escritório.</p>
    <div class="abertura-botoes" style="margin-top:36px">
      <a class="botao botao-principal" href="/">Ir para a página inicial</a>
      <a class="botao botao-contorno" href="{whats(c.WHATS_ANDERSON)}" target="_blank" rel="noopener">Conversar pelo WhatsApp</a>
    </div>
  </div>
</section>"""
    return documento(r, "404.html", f"Página não encontrada | {c.NOME}", "Página não encontrada.", corpo)


def sitemap() -> str:
    caminhos = [""] + [f"{a['slug']}/" for a in c.AREAS] + ["privacidade/"]
    urls = "\n".join(f"  <url><loc>{c.DOMINIO}/{p}</loc><lastmod>2026-11-25</lastmod></url>" for p in caminhos)
    return f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}\n</urlset>\n'


def gravar(caminho: str, texto: str) -> None:
    destino = RAIZ / caminho
    destino.parent.mkdir(parents=True, exist_ok=True)
    destino.write_text(texto, encoding="utf-8")
    print("gerado:", caminho)


def main() -> None:
    gravar("index.html", pagina_inicial())
    for area in c.AREAS:
        gravar(f"{area['slug']}/index.html", pagina_area(area))
    gravar("privacidade/index.html", pagina_privacidade())
    gravar("404.html", pagina_404())
    gravar("sitemap.xml", sitemap())
    gravar("robots.txt", f"User-agent: *\nAllow: /\nSitemap: {c.DOMINIO}/sitemap.xml\n")
    gravar("CNAME", "www.alvesarruda.com.br\n")


if __name__ == "__main__":
    main()
