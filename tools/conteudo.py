"""Dados e textos do site. Altere aqui e rode: python3 tools/gerar_paginas.py"""

DOMINIO = "https://www.alvesarruda.com.br"
NOME = "Alves & Arruda Advogados"
EMAIL = "alvesarrudaadvogados@gmail.com"
WHATS_ANDERSON = "5562985109393"
WHATS_ROBERTA = "5562982624401"
TELEFONE_ANDERSON = "(62) 98510-9393"
TELEFONE_ROBERTA = "(62) 98262-4401"
ENDERECO_LINHAS = [
    "Avenida E, número 1470, sala 608",
    "Edifício JK New Concept, Jardim Goiás",
    "Goiânia, Goiás, CEP 74810-030",
]
HORARIO = "Segunda a sexta, das 8h às 18h"
MAPA_BUSCA = "Avenida E 1470, Edifício JK New Concept, Jardim Goiás, Goiânia"
INSTAGRAM_ANDERSON = "https://www.instagram.com/andersonarrudaadvogado"
INSTAGRAM_ROBERTA = "https://www.instagram.com/robertaalvesadvogada"

# Ícones de traço fino (24 x 24)
ICONES = {
    "familia": '<path d="M7 8.5a2.5 2.5 0 1 0 0-5 2.5 2.5 0 0 0 0 5Zm10 0a2.5 2.5 0 1 0 0-5 2.5 2.5 0 0 0 0 5ZM12 14a2 2 0 1 0 0-4 2 2 0 0 0 0 4ZM3 20v-5.5A3.5 3.5 0 0 1 6.5 11h1a3.5 3.5 0 0 1 2 .6M21 20v-5.5a3.5 3.5 0 0 0-3.5-3.5h-1a3.5 3.5 0 0 0-2 .6M9 20v-2a3 3 0 0 1 6 0v2"/>',
    "medico": '<path d="M6 3v5a4 4 0 0 0 8 0V3M6 3H4.5M14 3h1.5M10 12v3a5 5 0 0 0 10 0v-1.5"/><circle cx="20" cy="11.5" r="2"/>',
    "inclusao": '<path d="M12 20s-7-4.4-7-10a4 4 0 0 1 7-2.6A4 4 0 0 1 19 10c0 5.6-7 10-7 10Z"/><path d="M9.5 11.5h5M12 9v5"/>',
    "civil": '<path d="M12 3v18M7 21h10M5 7h14M5 7l-3 7a3 3 0 0 0 6 0L5 7Zm14 0-3 7a3 3 0 0 0 6 0l-3-7Z"/>',
    "empresarial": '<rect x="3" y="7" width="18" height="13" rx="1.5"/><path d="M9 7V5a1.5 1.5 0 0 1 1.5-1.5h3A1.5 1.5 0 0 1 15 5v2M3 12.5h18M10.5 12.5v2h3v-2"/>',
}

AREAS = [
    {
        "slug": "familia",
        "icone": "familia",
        "titulo": "Família, Sucessões e Patrimônio",
        "resumo": "Conflitos familiares envolvem filhos, patrimônio, projetos de vida e relações construídas ao longo dos anos. Nossa atuação começa pela compreensão dessa realidade.",
        "chamada_titulo": "Organizar a família e o patrimônio <em>com clareza e cuidado.</em>",
        "introducao": "Separações, guarda dos filhos, pensão alimentícia, inventários e planejamento patrimonial são momentos que pedem técnica e sensibilidade. Cada família tem sua história, e a orientação jurídica precisa respeitar essa história para reduzir o desgaste e proteger o que foi construído.",
        "como": [
            "Ouvimos com atenção para entender a dinâmica familiar, as prioridades e as preocupações de cada pessoa envolvida.",
            "Sempre que possível, buscamos soluções consensuais, como acordos e mediação, que costumam ser mais rápidas e menos desgastantes.",
            "Quando o processo judicial é necessário, conduzimos o caso com estratégia, firmeza e comunicação constante.",
        ],
        "situacoes": [
            "Divórcio consensual ou litigioso, em cartório ou na Justiça",
            "Reconhecimento e dissolução de união estável",
            "Guarda, convivência e regulamentação de visitas",
            "Fixação, revisão e cobrança de pensão alimentícia",
            "Partilha de bens e proteção do patrimônio",
            "Inventário judicial e extrajudicial",
            "Testamentos, doações e planejamento sucessório",
            "Pactos antenupciais e contratos de convivência",
        ],
        "mensagem": "Olá! Gostaria de orientação sobre Direito de Família.",
        "whats": WHATS_ANDERSON,
    },
    {
        "slug": "direito-medico",
        "icone": "medico",
        "titulo": "Direito Médico e da Saúde",
        "resumo": "Assessoria jurídica para médicos, odontólogos, clínicas e demais profissionais da saúde, com atenção técnica, preventiva e estratégica.",
        "chamada_titulo": "Segurança jurídica <em>para quem cuida de outras pessoas.</em>",
        "introducao": "A rotina de quem atua na saúde envolve responsabilidades técnicas, éticas e jurídicas. Uma documentação bem organizada e uma orientação preventiva reduzem vulnerabilidades e dão tranquilidade para que o profissional se concentre no atendimento.",
        "como": [
            "Analisamos a rotina do consultório ou da clínica para identificar pontos de risco na documentação e nos contratos.",
            "Elaboramos e revisamos termos de consentimento, contratos e protocolos de atendimento.",
            "Acompanhamos o profissional em processos éticos, administrativos e judiciais, com estratégia técnica.",
        ],
        "situacoes": [
            "Termos de consentimento livre e esclarecido",
            "Contratos entre profissionais, clínicas e parceiros",
            "Defesa em processos ético-profissionais nos conselhos de classe",
            "Defesa em ações de responsabilidade civil",
            "Adequação de clínicas à Lei Geral de Proteção de Dados",
            "Constituição e organização societária de clínicas",
            "Orientação preventiva sobre prontuário e documentação",
        ],
        "mensagem": "Olá! Gostaria de orientação sobre Direito Médico e da Saúde.",
        "whats": WHATS_ROBERTA,
    },
    {
        "slug": "saude-autismo-inclusao",
        "icone": "inclusao",
        "titulo": "Saúde, Autismo e Inclusão",
        "resumo": "Atuação voltada ao acesso à saúde, aos tratamentos e à inclusão de pessoas com Transtorno do Espectro Autista e de suas famílias.",
        "chamada_titulo": "Acesso à saúde e à inclusão <em>como direito.</em>",
        "introducao": "Famílias de pessoas com Transtorno do Espectro Autista, com deficiência ou com doenças graves muitas vezes enfrentam negativas de tratamento, demora no atendimento e barreiras na escola. A Constituição Federal garante o direito à saúde e à educação inclusiva, e a legislação específica, como a Lei 12.764 de 2012 e a Lei Brasileira de Inclusão (Lei 13.146 de 2015), detalha essas garantias.",
        "como": [
            "Analisamos o caso, a prescrição médica e as respostas do plano de saúde, do poder público ou da escola.",
            "Buscamos primeiro a solução administrativa, com requerimentos e notificações bem fundamentados.",
            "Quando necessário, levamos o caso à Justiça, inclusive com pedidos de urgência.",
        ],
        "situacoes": [
            "Negativa de cobertura de terapias pelo plano de saúde",
            "Fornecimento de medicamentos e tratamentos pelo poder público",
            "Reajustes abusivos e cancelamento de planos de saúde",
            "Inclusão escolar e direito a acompanhante especializado",
            "Benefícios e direitos assegurados à pessoa com deficiência",
            "Orientação às famílias sobre direitos e documentação",
        ],
        "mensagem": "Olá! Gostaria de orientação sobre direitos de saúde, autismo e inclusão.",
        "whats": WHATS_ROBERTA,
    },
    {
        "slug": "civil-consumidor",
        "icone": "civil",
        "titulo": "Direito Civil e do Consumidor",
        "resumo": "Análise cuidadosa das relações pessoais, contratuais e patrimoniais para orientar decisões com responsabilidade.",
        "chamada_titulo": "Contratos claros e direitos <em>respeitados.</em>",
        "introducao": "Contratos, compras, imóveis, dívidas e danos fazem parte da vida de qualquer pessoa. Uma análise jurídica feita no momento certo evita prejuízos e, quando o conflito já existe, organiza o caminho mais seguro para resolvê-lo.",
        "como": [
            "Lemos com atenção contratos e documentos antes da assinatura, apontando riscos em linguagem simples.",
            "Buscamos a negociação e a solução amigável sempre que ela atender ao interesse do cliente.",
            "Conduzimos ações judiciais com base nos fatos, nos documentos e na legislação aplicável.",
        ],
        "situacoes": [
            "Elaboração e revisão de contratos",
            "Cobranças indevidas, negativação e problemas com bancos",
            "Defeitos em produtos e falhas na prestação de serviços",
            "Indenização por danos materiais e morais",
            "Compra, venda e locação de imóveis",
            "Cobrança de valores e execução de contratos",
        ],
        "mensagem": "Olá! Gostaria de orientação sobre Direito Civil ou do Consumidor.",
        "whats": WHATS_ANDERSON,
    },
    {
        "slug": "empresarial",
        "icone": "empresarial",
        "titulo": "Empresarial e Assessoria Jurídica",
        "resumo": "Apoio jurídico a empresas e profissionais, tanto na prevenção de riscos quanto na condução de conflitos.",
        "chamada_titulo": "Prevenção de riscos e <em>previsibilidade para o seu negócio.</em>",
        "introducao": "Um contrato bem redigido evita conflitos entre sócios, clientes e fornecedores. A assessoria jurídica contínua permite que a empresa tome decisões com segurança, antecipe riscos e reduza custos com litígios.",
        "como": [
            "Conhecemos a operação da empresa para entender riscos, rotinas e objetivos.",
            "Estruturamos contratos, acordos de sócios e documentos internos sob medida.",
            "Acompanhamos a empresa de forma contínua ou em demandas pontuais, com comunicação direta.",
        ],
        "situacoes": [
            "Constituição, alteração e encerramento de empresas",
            "Acordos de sócios e planejamento sucessório empresarial",
            "Contratos com clientes, fornecedores e parceiros",
            "Assessoria jurídica preventiva e consultiva mensal",
            "Cobrança e recuperação de créditos",
            "Negociação e condução de conflitos empresariais",
        ],
        "mensagem": "Olá! Gostaria de orientação sobre assessoria jurídica para empresas.",
        "whats": WHATS_ANDERSON,
    },
]

PRINCIPIOS = [
    ("Atendimento próximo", "Escutamos com atenção para compreender a situação, as prioridades e as expectativas de cada cliente."),
    ("Estratégia individualizada", "Cada situação tem seus fatos, documentos, riscos e objetivos. A análise considera essas particularidades."),
    ("Comunicação clara", "Traduzimos questões jurídicas complexas para uma linguagem objetiva e acessível."),
    ("Advocacia preventiva", "Quando possível, organizamos relações e documentos para reduzir riscos e evitar conflitos."),
    ("Atuação técnica", "A estratégia se apoia na análise dos fatos, dos documentos e das normas e decisões aplicáveis."),
]
GOOGLE_VERIFICACAO = "dWBzxlwmuNc7BcXcEHp_i7Mlz_Ma6tdE48Gez5xDyZk"
