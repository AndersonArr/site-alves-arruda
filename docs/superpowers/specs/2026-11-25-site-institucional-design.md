# Site institucional do Alves & Arruda Advogados: projeto

Data: 25 de novembro de 2026
Domínio: www.alvesarruda.com.br (novo, registrado no Registro.br em nome do escritório)

## 1. Intenção

O escritório precisa de um site **sob o próprio controle**. O site antigo (www.alvesearruda.com.br) foi hospedado por um terceiro com quem não há mais contato, de modo que o escritório não consegue alterá-lo nem criar novas páginas.

O novo site deve:
- ser moderno, bonito e robusto, com um visual calmo que deixe o visitante à vontade;
- usar a identidade oficial do escritório (cores, logomarca e fotos reais);
- seguir a estrutura e o tom do site antigo, que o Dr. Anderson aprova;
- servir de base para landing pages futuras, ligadas ao mesmo domínio.

O que o visitante deve fazer: conhecer o escritório e os sócios, encontrar a sua área de atuação e **iniciar uma conversa pelo WhatsApp**.

## 2. Objetivos, não objetivos e antiobjetivos

**Objetivos**
- Site de página principal longa, no padrão do site antigo, com páginas próprias para cada área de atuação.
- Todas as contas (código e hospedagem) em nome e no e-mail do escritório.
- Abrir rápido no celular, que é de onde vem a maior parte das visitas.
- Estrutura pronta para receber landing pages (exemplo: alvesarruda.com.br/divorcio).

**Não objetivos (nesta etapa)**
- Blog ou área de artigos.
- Painel para o escritório editar textos sozinho.
- Formulário com envio de e-mail, área do cliente e agendamento online.
- Versões em outros idiomas.

**Antiobjetivos (seria um fracasso mesmo que funcionasse)**
- Depender de outra pessoa ou empresa para ter acesso ao site.
- Linguagem de propaganda, promessa de resultado, divulgação de honorários ou identificação de clientes, em desacordo com o Provimento 205 de 2021 do Conselho Federal da Ordem dos Advogados do Brasil (VERIFICAR a versão vigente antes de publicar).
- Visual carregado: cores fora da paleta, gradientes chamativos ou excesso de animação.

## 3. Restrições

- Paleta oficial: marrom #322620 e dourado #FFB980, com os tons de apoio da identidade (#DCA06F, #F6E9DA, #6B5244, #FBF6EF). Dourado pêssego nunca aparece como texto sobre fundo claro.
- Tipografia: títulos em Playfair Display, com itálico nos destaques. No máximo 2 (duas) famílias de fonte.
- Logomarca usada sem alteração.
- Textos sem abreviações, com números em algarismo seguidos do extenso entre parênteses, conforme as regras de escrita do escritório. Exceção: "OAB/GO" junto ao nome dos sócios.
- Sem custo mensal além do domínio.

## 4. Abordagens consideradas

| Abordagem | Custo | Resultado |
|---|---|---|
| **A. Site em código próprio, hospedado em conta do escritório (escolhida)** | Gratuito | Visual livre e rápido, controle total. Alterações feitas pelo Claude ou por qualquer desenvolvedor |
| B. WordPress em hospedagem paga | Mensalidade | Edição por painel, mas site mais pesado e com manutenção de segurança |
| C. Wix ou Framer | Mensalidade maior | Edição visual, mas site preso à plataforma |

O Dr. Anderson escolheu a abordagem A e deixou a escolha da hospedagem com o Claude.

## 5. Como será feito (decisões técnicas, chamadas do Claude)

- **Tecnologia:** HTML, CSS e JavaScript puros, sem etapa de compilação. Qualquer desenvolvedor consegue abrir e alterar, e o site não "quebra" com o tempo por falta de atualização.
- **Hospedagem: GitHub Pages.** É gratuita, inclui certificado de segurança (o cadeado do https) e aceita domínio próprio. Exige uma única conta (GitHub), o que é mais simples do que manter 2 (duas). O código fica no mesmo lugar, com histórico de cada alteração.
- **Domínio:** o próprio escritório altera os registros de DNS no Registro.br, seguindo um passo a passo escrito pelo Claude. Nenhuma senha é compartilhada.
- **Fotos:** vêm da pasta "cliente / Anderson / Mentoria / fotos" do Google Drive, com 15 (quinze) arquivos. Serão otimizadas para a internet, ficando mais leves sem perda visível de qualidade.
- **Fontes:** Playfair Display nos títulos e uma fonte sem serifa de boa leitura, DM Sans, no corpo do texto. A DM Sans é a mesma do site antigo.

## 6. Estrutura do site

### Página principal (rolagem única, nesta ordem)

1. **Cabeçalho fixo:** logomarca, menu (O escritório, Atuação, Sócios, Contato) e botão "Fale conosco", que abre o WhatsApp.
2. **Abertura em tela cheia com a foto da fachada do prédio** (Edifício JK New Concept), no modelo do site do Jacó Coelho Advogados, a pedido do Dr. Anderson. Sobre a foto, uma película marrom (#322620) em degradê suave garante a leitura. Por cima vêm o título em Playfair Display ("Estratégia jurídica para proteger *o que importa*.", aproveitado do site antigo) e 2 (dois) botões: conversar pelo WhatsApp e ver as áreas. A foto dos sócios passa para a seção "O escritório".
3. **Faixa de destaques:** "Advocacia desde 2013", "Atendimento presencial e online em todo o Brasil" e "5 (cinco) áreas de atuação". Apenas números verdadeiros e verificáveis, sem contagem de processos ou de vitórias.
4. **Faixa com as áreas passando em movimento lento**, inspirada no site do Jacó Coelho Advogados.
5. **O escritório:** foto dos sócios trabalhando juntos e texto do site antigo ("Mais do que conhecer a lei…"), revisado com as regras de escrita.
6. **Áreas de atuação:** 5 (cinco) cartões, cada um levando à página da área:
   - Família, Sucessões e Patrimônio
   - Direito Médico e da Saúde
   - Saúde, Autismo e Inclusão
   - Direito Civil e do Consumidor
   - Empresarial e Assessoria Jurídica
7. **Destaque de uma área** (Direito Médico e da Saúde), com a foto da Dra. Roberta, como no site antigo.
8. **Nossa forma de trabalhar:** os 5 (cinco) princípios do site antigo.
9. **Os sócios:** fotos, inscrição na Ordem dos Advogados do Brasil, formação, foco de atuação e link para o Instagram de cada um.
10. **Nosso espaço:** galeria com a fachada e os ambientes do escritório.
11. **Contato:** os 2 (dois) WhatsApp, endereço com mapa, horário e e-mail.
12. **Rodapé:** logomarca, contatos, links e política de privacidade.
13. **Botão flutuante do WhatsApp** em todas as páginas.

### Outras páginas

- Uma página para cada área de atuação (`/familia`, `/direito-medico` e assim por diante), com explicação em linguagem simples, situações em que o escritório pode ajudar e chamada para o WhatsApp. Essas páginas ajudam o site a aparecer no Google e servem de modelo para as landing pages.
- Política de privacidade, exigida pela Lei Geral de Proteção de Dados (Lei 13.709 de 2018).
- Página de "não encontrado" (erro 404) com a identidade do escritório.

### Visual

- Alternância de seções em marrom (#322620) e em branco quente ou areia (#FBF6EF, #F6E9DA), como no ritmo do site antigo, agora nas cores oficiais.
- Filete dourado sob os títulos, inspirado na linha da logomarca.
- Animações discretas: elementos que surgem suavemente ao rolar e a faixa das áreas em movimento. As animações são desativadas automaticamente para quem configura o aparelho para reduzir movimento.

### Preparação para o Google

- Título e descrição de cada página, dados estruturados de "escritório de advocacia" com endereço e horário, mapa do site e imagem de compartilhamento para o WhatsApp e as redes sociais.

## 7. Dados confirmados pelo Dr. Anderson

- Horário de atendimento: segunda a sexta, das 8h às 18h.
- Endereço: Avenida E, número 1470, sala 608, Edifício JK New Concept, Jardim Goiás, Goiânia, Goiás, CEP 74810-030.
- Logomarca: 4 (quatro) arquivos enviados (completa quadrada, somente o símbolo, faixa clara e faixa escura), guardados em `assets/logo/`. Como os arquivos são pequenos (372 pixels), o desenvolvedor deve redesenhá-los em formato vetorial (SVG), com fidelidade total ao original, para que fiquem nítidos em qualquer tela. A versão original é a referência e não pode ser alterada.

## 8. O que fica a cargo do desenvolvedor

- Escolha e recorte das fotos para cada seção.
- Revisão final dos textos com as regras de escrita do escritório.
- Detalhes de espaçamento, tamanhos e animações, dentro da identidade.
- Publicação no GitHub Pages e o passo a passo do DNS para o escritório.

## 9. Etapas para o escritório

1. Criar uma conta gratuita no GitHub com o e-mail do escritório, ou autorizar o Claude a usar uma existente.
2. Aprovar o site em versão de prévia.
3. Alterar o DNS no Registro.br, seguindo o passo a passo.
