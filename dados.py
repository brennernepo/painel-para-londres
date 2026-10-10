"""Conteúdo do painel. O app lê tudo daqui; para corrigir ou incluir algo, edite este arquivo.

Preços conferidos em outubro de 2026. Ingressos mudam com a data e a TfL reajusta tarifas todo março,
então trate os valores como referência e confira no site oficial antes de comprar.
"""

from datetime import date

# Datas da viagem, usadas na aba Tempo & luz
VIAGEM_INICIO = date(2026, 10, 29)
VIAGEM_FIM = date(2026, 11, 2)

# Ponto de referência para previsão e horários do sol: centro de Londres
LOCAL_TEMPO = (51.51, -0.13)

# Cores oficiais das linhas da TfL
LINHAS = {
    "Bakerloo": "#B36305",
    "Central": "#E32017",
    "Circle": "#FFD300",
    "District": "#00782A",
    "Elizabeth": "#6950A1",
    "Hammersmith & City": "#F3A9BB",
    "Jubilee": "#A0A5A9",
    "Metropolitan": "#9B0056",
    "Northern": "#000000",
    "Piccadilly": "#003688",
    "Victoria": "#0098D4",
    "Waterloo & City": "#95CDBA",
    "DLR": "#00A4A7",
    "Overground": "#EE7C0E",
}

NIVEIS_SEGURANCA = {
    "verde": "Tranquilo para turistas",
    "atencao": "Atenção à noite",
    "evitar": "Evitar à noite",
}

# ---------------------------------------------------------------------------
# Regiões: cada ponto famoso abre a região a que pertence.
# Cada item de "pontos" é (emoji, nome, texto, tags) ou (emoji, nome, texto, tags, busca no Maps),
# quando o nome sozinho não acha o lugar no Google Maps.
# ---------------------------------------------------------------------------
REGIOES = {
    "westminster": {
        "nome": "Westminster & St James's",
        "filtro": "Westminster",
        "seguranca": "verde",
        "descricao": (
            "Parlamento, abadia, palácio e os parques reais, tudo a uma caminhada de distância. "
            "Concentra a maior parte dos cartões-postais e, por isso, a maior parte dos batedores de carteira."
        ),
        "metro": [
            ("Westminster", ["Jubilee", "District", "Circle"]),
            ("St James's Park", ["District", "Circle"]),
            ("Green Park", ["Jubilee", "Piccadilly", "Victoria"]),
            ("Victoria", ["Victoria", "District", "Circle"]),
        ],
        "pontos": [
            ("👑", "Buckingham Palace",
             "Residência oficial do rei. A Troca da Guarda começa às 11h, mas não acontece todo dia: o calendário "
             "sai no site da Household Division. As State Rooms só abrem para visita no verão, de julho a setembro.",
             ["Exterior grátis", "State Rooms pagas", "Guarda às 11h"]),
            ("🕐", "Big Ben e Palácio de Westminster",
             "Big Ben é o sino; a torre se chama Elizabeth Tower. O Parlamento vende visitas guiadas aos sábados "
             "e em parte dos recessos. Subir na torre é permitido só a residentes do Reino Unido.",
             ["Exterior grátis", "Tour do Parlamento pago"], "Big Ben"),
            ("⛪", "Westminster Abbey",
             "Coroações desde 1066 e os túmulos de Isaac Newton e Charles Darwin. Aos domingos não abre para "
             "turismo, só para missas, que são abertas a qualquer pessoa.",
             ["Pago", "Domingo só missa", "Compre online"]),
            ("🌿", "St James's Park",
             "Os pelicanos do lago comem entre 14h30 e 15h. Da ponte azul no meio do parque se vê o palácio "
             "de um lado e a Horse Guards do outro.",
             ["Grátis", "Pelicanos 14h30"]),
            ("🐎", "Horse Guards Parade",
             "Troca da guarda montada às 11h de segunda a sábado e às 10h no domingo, com bem menos gente "
             "que a do palácio.",
             ["Grátis", "11h (domingo 10h)"]),
            ("🦁", "Trafalgar Square",
             "Coluna de Nelson, os quatro leões e o Fourth Plinth, pedestal que recebe uma obra contemporânea "
             "nova mais ou menos a cada dois anos.",
             ["Grátis"]),
            ("🎨", "National Gallery",
             "Os Girassóis de Van Gogh, Turner, Velázquez, Leonardo. A coleção permanente é gratuita; "
             "as exposições temporárias, pagas.",
             ["Grátis", "Reserve 2h"]),
            ("🛡", "Churchill War Rooms",
             "O bunker de onde Churchill comandou a guerra, preservado como ficou em 1945. A fila é longa: "
             "compre com hora marcada.",
             ["Pago", "Compre antes"]),
        ],
        "dicas": [
            ("Troca da Guarda", "Chegue 45 minutos antes para pegar lugar na grade"),
            ("Westminster → Buckingham", "Uns 15 minutos a pé, cortando o St James's Park"),
            ("Foto do Big Ben", "Da Westminster Bridge ou da margem sul, em frente ao St Thomas' Hospital"),
            ("Jogo dos copinhos na ponte", "É golpe, com plateia combinada. Não aposte"),
        ],
    },
    "soho": {
        "nome": "Soho, Mayfair & Piccadilly",
        "filtro": "Soho & Mayfair",
        "seguranca": "verde",
        "descricao": (
            "Compras, teatros e restaurantes em poucos quarteirões. De dia é a Londres das vitrines; "
            "depois das 21h o Soho vira o centro da vida noturna."
        ),
        "metro": [
            ("Piccadilly Circus", ["Piccadilly", "Bakerloo"]),
            ("Oxford Circus", ["Central", "Victoria", "Bakerloo"]),
            ("Leicester Square", ["Piccadilly", "Northern"]),
            ("Bond Street", ["Central", "Jubilee", "Elizabeth"]),
        ],
        "pontos": [
            ("🎪", "Piccadilly Circus",
             "Os telões curvos e a estátua alada sobre a fonte, que todo mundo chama de Eros. Bom ponto de "
             "encontro e de partida para o resto da região.",
             ["Grátis", "Ponto de encontro"]),
            ("🛍", "Regent Street",
             "Avenida curva de fachadas iguais, com a Hamleys, loja de brinquedos fundada em 1760, e a Liberty "
             "logo atrás. As luzes de Natal acendem em novembro.",
             ["Compras", "Luzes em novembro"]),
            ("🛒", "Oxford Street",
             "Selfridges, John Lewis e as grandes redes em quase 2 km de calçada. No sábado à tarde mal dá "
             "para andar.",
             ["Compras", "Vá cedo"]),
            ("🎭", "West End",
             "Uns 40 teatros. O quiosque TKTS, na Leicester Square, vende ingressos que sobraram para o mesmo "
             "dia com desconto.",
             ["Preço varia muito", "TKTS no dia"], "Leicester Square"),
            ("🥟", "Chinatown",
             "Gerrard Street e arredores. Almoço barato e dim sum; no Ano-Novo Chinês tem desfile na região.",
             ["Barato", "Dim sum"]),
            ("🧥", "Carnaby Street",
             "A rua da moda dos anos 60, hoje com marcas independentes e o Kingly Court, pátio de "
             "restaurantes em três andares.",
             ["Lojas independentes", "Kingly Court"]),
            ("🫖", "Fortnum & Mason",
             "Armazém de 1707 na Piccadilly. Chás, biscoitos e cestas que viram presente; o térreo já basta "
             "para a visita.",
             ["Entrada livre", "Presentes"]),
            ("🖼", "National Portrait Gallery",
             "Reaberta em 2023 depois de reforma. Retratos de reis, cientistas e músicos britânicos, "
             "com entrada gratuita.",
             ["Grátis"]),
        ],
        "dicas": [
            ("Ingresso de musical", "TKTS na Leicester Square, para sessões do mesmo dia"),
            ("Oxford Street vazia", "Em dia útil, antes das 11h"),
            ("Jantar antes do teatro", "Menus pre-theatre, servidos entre 17h e 18h30, custam menos"),
            ("Banheiro", "Selfridges e John Lewis têm banheiros para clientes e visitantes"),
        ],
    },
    "southbank": {
        "nome": "South Bank & Bankside",
        "filtro": "South Bank",
        "seguranca": "verde",
        "descricao": (
            "A margem sul do Tâmisa, do London Eye à Tower Bridge. Tudo se faz a pé pela beira do rio: "
            "museu gratuito, mercado de comida e a City inteira do outro lado."
        ),
        "metro": [
            ("Waterloo", ["Jubilee", "Northern", "Bakerloo", "Waterloo & City"]),
            ("Southwark", ["Jubilee"]),
            ("London Bridge", ["Jubilee", "Northern"]),
        ],
        "pontos": [
            ("🎡", "London Eye",
             "Roda-gigante de 135 m; a volta completa leva cerca de 30 minutos. Online sai mais barato que "
             "na bilheteria, e o fim de tarde é o horário mais disputado.",
             ["Pago", "Online é mais barato", "30 min"]),
            ("🎨", "Tate Modern",
             "Arte moderna numa antiga usina elétrica. Grátis. O 10º andar do prédio Blavatnik tem um "
             "terraço com vista para a cidade toda.",
             ["Grátis", "Terraço no 10º andar"]),
            ("🎭", "Shakespeare's Globe",
             "Reconstrução do teatro de 1599, a céu aberto. Assistir em pé, na plateia, custa uma fração do "
             "preço dos assentos. Temporada de abril a outubro.",
             ["Em pé é barato", "Abril a outubro"]),
            ("🍖", "Borough Market",
             "Mercado de comida que funciona há séculos embaixo dos trilhos do trem. Vá com fome e antes do "
             "meio-dia; na segunda abrem poucas bancas.",
             ["Comida", "Vá cedo"]),
            ("🏙", "The Shard",
             "O prédio mais alto do Reino Unido, com mirante entre os andares 68 e 72. O preço muda conforme "
             "a data e o horário.",
             ["Pago", "Mirante 68º–72º"]),
            ("⚓", "HMS Belfast",
             "Navio de guerra de 1938 ancorado no rio, aberto da casa de máquinas à ponte de comando.",
             ["Pago", "Bom com crianças"]),
            ("🌉", "Tower Bridge",
             "Atravessar a pé é grátis. A exposição paga sobe às passarelas altas, que têm um trecho de piso "
             "de vidro.",
             ["Travessia grátis", "Piso de vidro pago"]),
        ],
        "dicas": [
            ("Caminhada", "Queen's Walk, do London Eye à Tower Bridge: uns 3,5 km"),
            ("Vista sem pagar", "Terraço da Tate Modern"),
            ("Para atravessar", "A Millennium Bridge, só de pedestres, liga a Tate à St Paul's"),
            ("Ponte levantando", "Os horários de abertura da Tower Bridge saem no site dela"),
        ],
    },
    "city": {
        "nome": "City of London",
        "filtro": "City of London",
        "seguranca": "verde",
        "descricao": (
            "O centro financeiro, construído sobre a Londres romana. Arranha-céus dividem a rua com igrejas "
            "de Christopher Wren, e no fim de semana o bairro quase esvazia."
        ),
        "metro": [
            ("Tower Hill", ["District", "Circle"]),
            ("St Paul's", ["Central"]),
            ("Bank", ["Central", "Northern", "Waterloo & City", "DLR"]),
            ("Liverpool Street", ["Elizabeth", "Central", "Circle", "Hammersmith & City", "Metropolitan"]),
        ],
        "pontos": [
            ("🏰", "Tower of London",
             "Fortaleza de quase mil anos que guarda as Joias da Coroa. Os Yeoman Warders conduzem visitas "
             "guiadas incluídas no ingresso.",
             ["Pago", "Joias da Coroa", "Chegue na abertura"]),
            ("⛪", "St Paul's Cathedral",
             "A cúpula de Wren, erguida depois do Grande Incêndio. A visita é paga; o Evensong, culto cantado "
             "no fim da tarde, tem entrada livre.",
             ["Pago", "Evensong grátis"]),
            ("🔭", "Sky Garden",
             "Jardim no topo do 20 Fenchurch Street, o prédio apelidado de Walkie-Talkie. Entrada grátis com "
             "reserva online, que esgota rápido.",
             ["Grátis com reserva", "Esgota"]),
            ("🏛", "Leadenhall Market",
             "Mercado coberto vitoriano, de teto pintado e ferro fundido. Aparece como o Beco Diagonal no "
             "primeiro filme de Harry Potter.",
             ["Grátis", "Cenário de Harry Potter"]),
            ("🌿", "St Dunstan-in-the-East",
             "Igreja bombardeada em 1941 que virou jardim entre as ruínas. Pequena e silenciosa, no meio "
             "dos escritórios.",
             ["Grátis", "Foto"]),
            ("🗼", "The Monument",
             "Coluna de 61 m em memória do Grande Incêndio de 1666. São 311 degraus até o mirante.",
             ["Barato", "311 degraus"]),
        ],
        "dicas": [
            ("Fim de semana", "Muitos restaurantes da City fecham no sábado e no domingo"),
            ("Sky Garden", "Reserve assim que as datas abrirem no site"),
            ("Tower of London", "Vá direto às Joias da Coroa, antes da fila crescer"),
            ("Tower Hill → Tower Bridge", "5 minutos a pé"),
        ],
    },
    "covent": {
        "nome": "Covent Garden & Bloomsbury",
        "filtro": "Covent Garden",
        "seguranca": "verde",
        "descricao": (
            "A praça dos artistas de rua, a Royal Opera House e, subindo para o norte, o British Museum e as "
            "ruas de livrarias de Bloomsbury."
        ),
        "metro": [
            ("Covent Garden", ["Piccadilly"]),
            ("Leicester Square", ["Piccadilly", "Northern"]),
            ("Holborn", ["Central", "Piccadilly"]),
            ("Tottenham Court Road", ["Central", "Northern", "Elizabeth"]),
        ],
        "pontos": [
            ("🏛", "British Museum",
             "Pedra de Roseta, múmias egípcias, os mármores do Partenon. Grátis e grande demais para um dia: "
             "escolha três ou quatro salas.",
             ["Grátis", "Reserve 3h"]),
            ("🎭", "Covent Garden Piazza",
             "Mercado coberto e artistas de rua o dia inteiro. As apresentações maiores ficam no lado oeste, "
             "em frente à igreja de St Paul.",
             ["Grátis", "Artistas de rua"]),
            ("🎼", "Royal Opera House",
             "Ópera e balé. Toda sexta o site libera ingressos baratos para a semana seguinte, o Friday Rush.",
             ["Preço varia", "Friday Rush"]),
            ("🚇", "London Transport Museum",
             "Ônibus vermelhos e vagões antigos do metrô. O ingresso vale para voltar quantas vezes quiser "
             "durante um ano.",
             ["Pago", "Vale 1 ano"]),
            ("🌈", "Neal's Yard",
             "Pátio pequeno de fachadas coloridas, escondido entre Covent Garden e Seven Dials.",
             ["Grátis", "Foto"]),
            ("📚", "Charing Cross Road",
             "A rua das livrarias, com a Foyles e sebos nas travessas, como a Cecil Court.",
             ["Livrarias"]),
        ],
        "dicas": [
            ("Estação Covent Garden", "Prefira Leicester Square, a 5 minutos: a de Covent Garden só tem elevador e lota"),
            ("British Museum", "A entrada dos fundos, na Montague Place, costuma ter fila menor"),
            ("Teatro barato", "O TKTS fica a 5 minutos, na Leicester Square"),
            ("Dia de chuva", "Mercado coberto e Transport Museum"),
        ],
    },
    "kensington": {
        "nome": "South Kensington & Knightsbridge",
        "filtro": "Kensington",
        "seguranca": "verde",
        "descricao": (
            "Três museus gratuitos lado a lado na Exhibition Road, o Hyde Park e a Harrods. A região mais "
            "fácil para um dia com crianças ou com chuva."
        ),
        "metro": [
            ("South Kensington", ["District", "Circle", "Piccadilly"]),
            ("Knightsbridge", ["Piccadilly"]),
            ("Hyde Park Corner", ["Piccadilly"]),
            ("High Street Kensington", ["District", "Circle"]),
        ],
        "pontos": [
            ("🦕", "Natural History Museum",
             "Esqueleto de baleia-azul no saguão, galeria de dinossauros com um T-rex que se mexe e a sala "
             "que simula um terremoto. Grátis.",
             ["Grátis", "Dinossauros"]),
            ("🎨", "V&A",
             "Design, moda, joias e esculturas. Grátis, com café e um pátio interno bom para descansar as pernas.",
             ["Grátis"]),
            ("🔬", "Science Museum",
             "Foguetes, motores a vapor e a cápsula da Apollo 10. A entrada é grátis; a área interativa "
             "Wonderlab é paga.",
             ["Grátis", "Wonderlab pago"]),
            ("🌳", "Hyde Park",
             "O lago Serpentine, o Speakers' Corner aos domingos e, emendado nele, o Kensington Gardens, "
             "com o palácio e o parquinho da Diana.",
             ["Grátis", "Pedalinho no verão"]),
            ("🛍", "Harrods",
             "A loja de departamentos de Knightsbridge. O Food Hall, no térreo, é a parte que justifica a "
             "visita mesmo sem comprar nada.",
             ["Entrada livre", "Food Hall"]),
            ("👑", "Kensington Palace",
             "Onde a princesa Diana morou e a rainha Vitória nasceu. A visita é paga; o jardim rebaixado do "
             "lado de fora é grátis.",
             ["Pago", "Jardim grátis"]),
            ("🎼", "Royal Albert Hall",
             "Casa de concertos de 1871. No verão recebe o BBC Proms, com ingressos em pé vendidos no dia "
             "por poucas libras.",
             ["Shows", "Proms no verão"]),
        ],
        "dicas": [
            ("Túnel dos museus", "Da estação South Kensington, um túnel leva aos museus sem pegar chuva"),
            ("Com crianças", "Comece pelo NHM na abertura, antes das excursões escolares"),
            ("Piquenique", "Compre no Food Hall da Harrods e coma no Hyde Park"),
            ("Atravessar o parque", "De Hyde Park Corner ao palácio, uns 40 minutos a pé"),
        ],
    },
    "nottinghill": {
        "nome": "Notting Hill",
        "filtro": "Notting Hill",
        "seguranca": "verde",
        "descricao": (
            "Casas coloridas, a Portobello Road e um bairro residencial que lota no sábado. Fora do dia de "
            "feira, é calmo e bom para andar sem pressa."
        ),
        "metro": [
            ("Notting Hill Gate", ["Central", "District", "Circle"]),
            ("Ladbroke Grove", ["Hammersmith & City", "Circle"]),
            ("Westbourne Park", ["Hammersmith & City", "Circle"]),
        ],
        "pontos": [
            ("🛒", "Portobello Road Market",
             "Feira de rua com antiguidades no sábado e comida e roupas nos outros dias. No domingo quase "
             "tudo fecha.",
             ["Sábado é o dia", "Domingo fechado"]),
            ("🏠", "Casas coloridas",
             "Lancaster Road, Westbourne Park Road e as travessas da Portobello. São casas de moradores: foto "
             "da calçada, sem subir na escada.",
             ["Grátis", "Casas privadas"], "Lancaster Road, Notting Hill"),
            ("🚪", "A porta do filme",
             "280 Westbourne Park Road, a casa do personagem de Hugh Grant em Um Lugar Chamado Notting Hill. "
             "A porta azul foi trocada e hoje é preta.",
             ["Grátis", "Cinema"], "280 Westbourne Park Road"),
            ("📚", "The Notting Hill Bookshop",
             "A livraria de viagem da Blenheim Crescent que inspirou a do filme.",
             ["Livraria"]),
            ("🎬", "Electric Cinema",
             "Um dos cinemas mais antigos do Reino Unido, aberto em 1910, com poltronas de couro e camas na "
             "primeira fila.",
             ["Cinema", "Desde 1910"]),
            ("🎉", "Notting Hill Carnival",
             "No fim de semana do feriado de agosto, o maior carnaval de rua da Europa. Multidão enorme: "
             "deixe objetos de valor no hotel.",
             ["Fim de agosto", "Lotado"], "Notting Hill"),
        ],
        "dicas": [
            ("Melhor horário", "Sábado antes das 10h, para pegar a feira sem multidão"),
            ("Chegada", "Notting Hill Gate, descendo a Pembridge Road até a Portobello"),
            ("Volta", "Ladbroke Grove, no fim da feira, para não subir a rua de novo"),
            ("Fotos das casas", "Cedo, com a rua vazia"),
        ],
    },
    "camden": {
        "nome": "Camden Town",
        "filtro": "Camden",
        "seguranca": "atencao",
        "descricao": (
            "Mercados, música ao vivo e o Regent's Canal. De dia é cheio e divertido; à noite, fique nas ruas "
            "movimentadas e recuse ofertas na saída do metrô."
        ),
        "metro": [
            ("Camden Town", ["Northern"]),
            ("Chalk Farm", ["Northern"]),
            ("Camden Road", ["Overground"]),
        ],
        "pontos": [
            ("🛒", "Camden Market",
             "Vários mercados colados: Stables, Camden Lock e Buck Street. Roupa, vinil, artesanato e comida "
             "de tudo quanto é país.",
             ["Grátis", "Comida de rua"]),
            ("🎤", "Estátua de Amy Winehouse",
             "Bronze em tamanho real no Stables Market, inaugurado em 2014 no dia em que ela faria 31 anos.",
             ["Grátis", "Stables Market"], "Amy Winehouse statue, Stables Market"),
            ("🚤", "Regent's Canal",
             "Trilha à beira do canal até Little Venice, cerca de uma hora a pé. O mesmo trecho de barco leva "
             "uns 50 minutos.",
             ["Grátis a pé", "Barco pago"], "Camden Lock"),
            ("🎸", "The Roundhouse",
             "Galpão de locomotivas de 1846 que virou casa de shows. Pink Floyd e The Doors tocaram lá nos "
             "anos 60.",
             ["Shows"]),
            ("🌳", "Primrose Hill",
             "Morro a uns 15 minutos do mercado, com vista do skyline inteiro. Grátis e bom para o pôr do sol.",
             ["Grátis", "Pôr do sol"]),
            ("🦁", "London Zoo",
             "No Regent's Park, a uns 20 minutos a pé do mercado. Pago; faz sentido para quem está com crianças.",
             ["Pago", "Com crianças"]),
        ],
        "dicas": [
            ("Metrô no domingo", "Camden Town pode virar só de saída à tarde; use Chalk Farm"),
            ("Onde comer", "Barracas do Camden Lock Market, à beira do canal"),
            ("À noite", "Fique na Camden High Street e na Chalk Farm Road"),
            ("Combinação", "Mercado de manhã, Primrose Hill no fim da tarde"),
        ],
    },
    "shoreditch": {
        "nome": "Shoreditch & Spitalfields",
        "filtro": "Shoreditch",
        "seguranca": "atencao",
        "descricao": (
            "Grafite em quase todo muro, a Brick Lane e os mercados de domingo. O bairro mais animado do "
            "leste, com noite agitada e travessas que esvaziam cedo."
        ),
        "metro": [
            ("Shoreditch High Street", ["Overground"]),
            ("Liverpool Street", ["Elizabeth", "Central", "Circle", "Hammersmith & City", "Metropolitan"]),
            ("Old Street", ["Northern"]),
            ("Aldgate East", ["District", "Hammersmith & City"]),
        ],
        "pontos": [
            ("🎨", "Street art",
             "Os muros da Brick Lane, da Hanbury Street e da Rivington Street mudam toda semana. Os tours "
             "guiados a pé duram umas duas horas.",
             ["Grátis", "Tour opcional"], "Brick Lane"),
            ("🥯", "Brick Lane",
             "Bagel de carne salgada no Beigel Bake, aberto 24 horas, e uma fileira de restaurantes de curry "
             "bengali.",
             ["Barato", "Beigel Bake 24h"]),
            ("🛍", "Old Spitalfields Market",
             "Mercado coberto vitoriano com moda, antiguidades e comida, aberto todos os dias.",
             ["Todos os dias"]),
            ("💐", "Columbia Road Flower Market",
             "Feira de flores só aos domingos, das 8h às 15h. No fim, os vendedores baixam o preço.",
             ["Só domingo", "Vá cedo"]),
            ("📦", "Boxpark Shoreditch",
             "Centro de lojas feito de contêineres, ao lado da estação, com comida no andar de cima.",
             ["Comida", "Ao lado da estação"]),
            ("🕯", "Dennis Severs' House",
             "Casa georgiana montada como se a família tivesse acabado de sair. Visita à luz de velas e em "
             "silêncio.",
             ["Pago", "Reserva"]),
        ],
        "dicas": [
            ("Melhor dia", "Domingo: Columbia Road de manhã, Brick Lane e Spitalfields à tarde"),
            ("À noite", "Fique nas ruas cheias; as travessas esvaziam depois das 23h"),
            ("Chegada", "Overground até Shoreditch High Street, ou Liverpool Street e 10 minutos a pé"),
            ("Fome de madrugada", "Beigel Bake"),
        ],
    },
    "greenwich": {
        "nome": "Greenwich",
        "filtro": "Greenwich",
        "seguranca": "verde",
        "descricao": (
            "A linha do meridiano, o veleiro Cutty Sark, um parque com vista para Canary Wharf e museus "
            "marítimos gratuitos. Ir de barco pelo Tâmisa já faz parte do passeio."
        ),
        "metro": [
            ("Cutty Sark", ["DLR"]),
            ("Greenwich", ["DLR"]),
            ("North Greenwich", ["Jubilee"]),
        ],
        "pontos": [
            ("🌍", "Royal Observatory",
             "Onde passa o meridiano de Greenwich. A foto com um pé em cada hemisfério é na área paga; "
             "o Planetário fica no mesmo terreno.",
             ["Pago", "Meridiano"], "Royal Observatory Greenwich"),
            ("⛵", "Cutty Sark",
             "Veleiro de 1869 que trazia chá da China. Dá para andar embaixo do casco, que fica suspenso.",
             ["Pago"]),
            ("🌳", "Greenwich Park",
             "Suba até a estátua do General Wolfe: dali se vê o rio, a Queen's House e os prédios de "
             "Canary Wharf.",
             ["Grátis", "Vista"]),
            ("🚢", "National Maritime Museum",
             "Navegação, explorações e a história da Marinha britânica. Grátis.",
             ["Grátis"]),
            ("🏛", "Queen's House",
             "Casa do século 17 com a escada em espiral Tulip Stairs. Grátis.",
             ["Grátis"]),
            ("🛍", "Greenwich Market",
             "Mercado coberto de artesanato e comida, aberto todos os dias.",
             ["Comida", "Todos os dias"]),
            ("🚡", "Teleférico IFS Cloud",
             "Cabine sobre o Tâmisa saindo de North Greenwich, com uns 10 minutos de travessia.",
             ["Pago", "Vista do rio"], "IFS Cloud Cable Car, North Greenwich"),
        ],
        "dicas": [
            ("Ida de barco", "Uber Boat by Thames Clippers, de Westminster ou da Tower; aceita contactless"),
            ("Túnel a pé", "O Greenwich Foot Tunnel passa por baixo do rio até Island Gardens"),
            ("Tempo", "Meio dia; o dia inteiro se for entrar em tudo"),
            ("Volta", "DLR em Cutty Sark leva a Canary Wharf em poucos minutos"),
        ],
    },
    "chelsea": {
        "nome": "Chelsea",
        "filtro": "Chelsea",
        "seguranca": "verde",
        "descricao": (
            "Bairro residencial elegante cortado pela King's Road. Galerias, o estádio do Chelsea e casas "
            "onde moraram músicos e escritores."
        ),
        "metro": [
            ("Sloane Square", ["District", "Circle"]),
            ("Fulham Broadway", ["District"]),
            ("South Kensington", ["District", "Circle", "Piccadilly"]),
        ],
        "pontos": [
            ("🛍", "King's Road",
             "A rua do punk nos anos 70, hoje de lojas e cafés. Começa na Sloane Square.",
             ["Compras"]),
            ("🎨", "Saatchi Gallery",
             "Arte contemporânea na Duke of York's Square. A maioria das exposições é gratuita.",
             ["Grátis na maioria"]),
            ("⚽", "Stamford Bridge",
             "Estádio do Chelsea FC. Tour pelo vestiário e museu do clube em dias sem jogo.",
             ["Tour pago"]),
            ("🎵", "42 Oakley Street",
             "Placa azul na casa onde Bob Marley morou em 1977, ano em que terminou o álbum Exodus em Londres.",
             ["Grátis", "Casa privada"], "42 Oakley Street, SW3"),
            ("🌿", "Chelsea Physic Garden",
             "Jardim botânico de 1673, um dos mais antigos da Inglaterra, dedicado a plantas medicinais.",
             ["Pago"]),
            ("🎖", "Royal Hospital Chelsea",
             "Lar dos veteranos de casaco vermelho, os Chelsea Pensioners. Em maio recebe a Chelsea Flower Show.",
             ["Jardins abertos", "Flower Show em maio"]),
        ],
        "dicas": [
            ("Uma tarde", "Saatchi, King's Road e Physic Garden"),
            ("Dia de jogo", "Fulham Broadway lota; evite o metrô perto do horário"),
            ("Flower Show", "Maio, com ingressos esgotando meses antes"),
            ("Chegada", "Sloane Square, na ponta da King's Road"),
        ],
    },
    "canary": {
        "nome": "Canary Wharf",
        "filtro": "Canary Wharf",
        "seguranca": "verde",
        "descricao": (
            "O segundo centro financeiro da cidade, erguido nas antigas docas. Arranha-céus, um jardim "
            "suspenso gratuito e o museu das docas. Limpo e calmo no fim de semana."
        ),
        "metro": [
            ("Canary Wharf", ["Jubilee", "Elizabeth", "DLR"]),
        ],
        "pontos": [
            ("🌿", "Crossrail Place Roof Garden",
             "Jardim sob uma cobertura de madeira, em cima da estação da Elizabeth Line. Grátis.",
             ["Grátis"]),
            ("🏙", "One Canada Square e as praças",
             "Os arranha-céus e as praças entre eles. À noite, os prédios iluminados rendem boas fotos.",
             ["Grátis", "Foto noturna"], "One Canada Square"),
            ("⚓", "Museum of London Docklands",
             "A história do porto e do comércio de Londres, num armazém de 1802. Grátis.",
             ["Grátis"]),
            ("✨", "Winter Lights",
             "Festival de instalações de luz em janeiro, ao ar livre e gratuito.",
             ["Janeiro", "Grátis"], "Canary Wharf"),
        ],
        "dicas": [
            ("Chegada rápida", "Elizabeth Line de Tottenham Court Road em uns 15 minutos"),
            ("Fim de semana", "Escritórios fechados, praças vazias"),
            ("Combinação", "DLR até Greenwich em menos de 15 minutos"),
        ],
    },
}

# ---------------------------------------------------------------------------
# Pontos famosos (a grade da primeira aba). Cada um aponta para uma região.
# ---------------------------------------------------------------------------
MARCOS = [
    ("buckingham", "👑", "Buckingham Palace", "westminster"),
    ("bigben", "🕐", "Big Ben", "westminster"),
    ("abbey", "⛪", "Westminster Abbey", "westminster"),
    ("trafalgar", "🦁", "Trafalgar Square", "westminster"),
    ("natgallery", "🎨", "National Gallery", "westminster"),
    ("piccadilly", "🎪", "Piccadilly Circus", "soho"),
    ("regent", "🛍", "Regent Street", "soho"),
    ("oxford", "🛒", "Oxford Street", "soho"),
    ("westend", "🎭", "West End / Teatros", "soho"),
    ("eye", "🎡", "London Eye", "southbank"),
    ("tate", "🖼", "Tate Modern", "southbank"),
    ("towerbridge", "🌉", "Tower Bridge", "southbank"),
    ("borough", "🍖", "Borough Market", "southbank"),
    ("shard", "🏙", "The Shard", "southbank"),
    ("tower", "🏰", "Tower of London", "city"),
    ("stpauls", "⛪", "St Paul's Cathedral", "city"),
    ("skygarden", "🔭", "Sky Garden", "city"),
    ("britishmuseum", "🏛", "British Museum", "covent"),
    ("coventgarden", "🎭", "Covent Garden", "covent"),
    ("nhm", "🦕", "Natural History Museum", "kensington"),
    ("hydepark", "🌳", "Hyde Park", "kensington"),
    ("harrods", "🛍", "Harrods", "kensington"),
    ("nottinghill", "🏠", "Notting Hill", "nottinghill"),
    ("portobello", "🛒", "Portobello Road", "nottinghill"),
    ("camdenmarket", "🛒", "Camden Market", "camden"),
    ("amy", "🎤", "Estátua de Amy Winehouse", "camden"),
    ("bricklane", "🎨", "Brick Lane / Street Art", "shoreditch"),
    ("columbia", "💐", "Columbia Road", "shoreditch"),
    ("meridiano", "🌍", "Greenwich / Meridiano", "greenwich"),
    ("cuttysark", "⛵", "Cutty Sark", "greenwich"),
    ("kingsroad", "🛍", "King's Road", "chelsea"),
    ("stamford", "⚽", "Stamford Bridge", "chelsea"),
    ("saatchi", "🎨", "Saatchi Gallery", "chelsea"),
    ("canarywharf", "🏙", "Canary Wharf", "canary"),
    ("roofgarden", "🌿", "Crossrail Roof Garden", "canary"),
]

# ---------------------------------------------------------------------------
# Rotas temáticas. Cada parada: (nome, endereço, estação, texto)
# ---------------------------------------------------------------------------
ROTAS = [
    {
        "id": "rock",
        "emoji": "🎸",
        "nome": "Rota do Rock",
        "chamada": "Abbey Road · Camden · Hendrix · Bob Marley",
        "descricao": (
            "Endereços dos Beatles, de Jimi Hendrix, Bob Marley e Amy Winehouse. Começa em St John's Wood, "
            "passa por Camden e pelo centro e termina em Chelsea."
        ),
        "duracao": "1 dia cheio · trechos a pé e de metrô",
        "paradas": [
            ("Abbey Road Studios e a faixa de pedestres", "3 Abbey Road, NW8 9AY", "St John's Wood (Jubilee)",
             "A faixa da capa de Abbey Road (1969) fica bem na frente dos estúdios. É rua de verdade, com carro "
             "passando: foto rápida e olho no trânsito. O muro dos estúdios é coberto de recados de fãs."),
            ("Estátua de Amy Winehouse", "Stables Market, Chalk Farm Road, NW1 8AH", "Chalk Farm (Northern)",
             "Bronze em tamanho real no Stables Market. Do Abbey Road dá para vir a pé atravessando o "
             "Primrose Hill, uns 40 minutos."),
            ("The Hawley Arms", "2 Castlehaven Road, NW1 8QU", "Camden Town (Northern)",
             "O pub que Amy frequentava, a poucos passos do mercado."),
            ("The Roundhouse", "Chalk Farm Road, NW1 8EH", "Chalk Farm (Northern)",
             "Galpão de locomotivas que virou palco em 1966, com Pink Floyd na noite de abertura. The Doors "
             "tocou lá em 1968."),
            ("Denmark Street", "Denmark Street, WC2H", "Tottenham Court Road (Central, Northern, Elizabeth)",
             "A antiga Tin Pan Alley de Londres, rua das lojas de guitarra. Os Sex Pistols moraram e ensaiaram "
             "no número 6."),
            ("Handel & Hendrix in London", "25 Brook Street, W1K 4HB", "Bond Street (Central, Jubilee, Elizabeth)",
             "O apartamento onde Jimi Hendrix morou em 1968 e 1969, colado à casa onde Handel viveu dois "
             "séculos antes. Hoje é museu, com visita paga."),
            ("42 Oakley Street", "42 Oakley Street, SW3", "Sloane Square (District, Circle)",
             "Placa azul na casa onde Bob Marley morou em 1977, ano do Exodus. É residência particular: "
             "só a fachada."),
        ],
    },
    {
        "id": "pubs",
        "emoji": "🍺",
        "nome": "Rota dos Pubs",
        "chamada": "Sete pubs históricos, de oeste a leste",
        "descricao": (
            "Pubs do século 17 ao art nouveau, cada um com sua história. Cabe num dia longo, mas o melhor é "
            "dividir em dois."
        ),
        "duracao": "1 a 2 dias · metrô entre os trechos",
        "paradas": [
            ("The Churchill Arms", "119 Kensington Church Street, W8 7LN", "Notting Hill Gate (Central, District, Circle)",
             "Fachada coberta de flores o ano inteiro e cozinha tailandesa nos fundos."),
            ("The Grenadier", "18 Wilton Row, SW1X 7NR", "Hyde Park Corner (Piccadilly)",
             "Escondido num beco de Belgravia, foi bar dos oficiais da guarda. Dizem que tem fantasma."),
            ("Lamb & Flag", "33 Rose Street, WC2E 9EB", "Covent Garden (Piccadilly)",
             "Um dos pubs mais antigos de Covent Garden, num beco estreito. Charles Dickens bebia ali."),
            ("Ye Olde Mitre", "1 Ely Court, EC1N 6SJ", "Chancery Lane (Central)",
             "Num corredor entre Hatton Garden e Ely Place, fácil de passar reto. O horário de fim de semana "
             "é reduzido: confira antes."),
            ("Ye Olde Cheshire Cheese", "145 Fleet Street, EC4A 2BU", "Chancery Lane (Central)",
             "Reconstruído logo depois do Grande Incêndio de 1666, com salas escuras em vários níveis."),
            ("The Black Friar", "174 Queen Victoria Street, EC4V 4EG", "Blackfriars (District, Circle)",
             "Interior art nouveau, com frades esculpidos em bronze e mármore pelas paredes."),
            ("The George Inn", "75 Borough High Street, SE1 1NH", "London Bridge (Jubilee, Northern)",
             "A última estalagem de Londres com galerias externas, do século 17. Pertence ao National Trust."),
        ],
    },
    {
        "id": "esporte",
        "emoji": "⚽",
        "nome": "Rota do Esporte",
        "chamada": "Wembley · Lord's · Arsenal · Tottenham · Chelsea · Wimbledon",
        "descricao": (
            "Tours por estádios de futebol, pelo templo do críquete e pelo museu de Wimbledon. Ficam longe "
            "um do outro: escolha dois ou três por dia."
        ),
        "duracao": "2 dias · todos os tours com reserva",
        "paradas": [
            ("Wembley Stadium", "Wembley, HA9 0WS", "Wembley Park (Jubilee, Metropolitan)",
             "Tour pelo vestiário da seleção inglesa, pelo túnel e pela tribuna de honra. Em dia de evento "
             "não tem tour."),
            ("Lord's Cricket Ground", "St John's Wood Road, NW8 8QN", "St John's Wood (Jubilee)",
             "A casa do críquete. O tour passa pelo Long Room e pelo museu onde fica a urna das Ashes."),
            ("Emirates Stadium", "Hornsey Road, N7 7AJ", "Arsenal (Piccadilly)",
             "Casa do Arsenal desde 2006, com tour pelo vestiário e museu do clube."),
            ("Tottenham Hotspur Stadium", "782 High Road, N17 0BX", "White Hart Lane (Overground)",
             "Estádio inaugurado em 2019. A atração Dare Skywalk leva os visitantes para cima do telhado."),
            ("Stamford Bridge", "Fulham Road, SW6 1HS", "Fulham Broadway (District)",
             "Casa do Chelsea, com tour e museu do clube."),
            ("Wimbledon", "Church Road, SW19 5AE", "Southfields (District)",
             "Museu do tênis e tour pelas quadras. Durante o torneio, entre o fim de junho e o começo de "
             "julho, o tour não funciona."),
        ],
    },
    {
        "id": "premium",
        "emoji": "✨",
        "nome": "Rota Premium",
        "chamada": "Chá no Ritz · Sketch · Harrods · terraços",
        "descricao": (
            "Chá da tarde clássico, restaurantes que são cenário e bares com vista. Tudo pede reserva, e "
            "alguns lugares têm código de vestimenta."
        ),
        "duracao": "2 dias · reservas com antecedência",
        "paradas": [
            ("Harrods", "87–135 Brompton Road, SW1X 7XL", "Knightsbridge (Piccadilly)",
             "Comece pelo Food Hall, no térreo."),
            ("The Ritz London", "150 Piccadilly, W1J 9BR", "Green Park (Jubilee, Piccadilly, Victoria)",
             "Chá da tarde no Palm Court, com reservas abertas meses antes. Homens precisam de paletó e "
             "gravata; jeans e tênis não entram."),
            ("Fortnum & Mason", "181 Piccadilly, W1A 1ER", "Piccadilly Circus (Piccadilly, Bakerloo)",
             "A poucos minutos do Ritz. O Diamond Jubilee Tea Salon foi inaugurado pela rainha em 2012."),
            ("sketch", "9 Conduit Street, W1S 2XG", "Oxford Circus (Central, Victoria, Bakerloo)",
             "Casa georgiana dividida em salões temáticos. Os banheiros em cápsulas em forma de ovo viram "
             "foto quase tanto quanto a comida."),
            ("The Landmark London", "222 Marylebone Road, NW1 6JQ", "Marylebone (Bakerloo)",
             "Chá da tarde no Winter Garden, átrio de oito andares com palmeiras."),
            ("Madison", "One New Change, EC4M 9AF", "St Paul's (Central)",
             "Terraço no alto do One New Change, de frente para a cúpula da St Paul's."),
            ("Duck & Waffle", "110 Bishopsgate, EC2N 4AY", "Liverpool Street (Elizabeth, Central)",
             "Restaurante no 40º andar, com elevador de vidro do lado de fora do prédio."),
        ],
    },
    {
        "id": "hp",
        "emoji": "⚡",
        "nome": "Rota Harry Potter",
        "chamada": "Plataforma 9¾ · Leadenhall · Millennium Bridge · Warner Bros",
        "descricao": (
            "Locações dos filmes no centro e o estúdio em Leavesden, onde estão os cenários. O estúdio pede "
            "um dia só para ele."
        ),
        "duracao": "1 dia na cidade + 1 dia no estúdio",
        "paradas": [
            ("Plataforma 9¾", "King's Cross Station, N1 9AP", "King's Cross St Pancras (várias linhas)",
             "O carrinho entrando na parede e a loja oficial ficam no saguão. Tirar a própria foto é grátis; "
             "cedo a fila anda mais rápido."),
            ("Claremont Square (Largo Grimmauld)", "Claremont Square, N1", "Angel (Northern)",
             "As fachadas georgianas usadas como o número 12 do Largo Grimmauld em A Ordem da Fênix."),
            ("Australia House (Gringotes)", "Strand, WC2B 4LA", "Temple (District, Circle)",
             "O saguão de mármore virou o banco Gringotes no primeiro filme. É prédio diplomático: só a fachada."),
            ("Millennium Bridge", "Millennium Bridge", "St Paul's (Central)",
             "A ponte que os Comensais da Morte derrubam no começo de O Enigma do Príncipe."),
            ("Leadenhall Market (Beco Diagonal)", "Gracechurch Street, EC3V 1LT", "Monument (District, Circle)",
             "Cenário do Beco Diagonal no primeiro filme. A porta azul da Bull's Head Passage foi a entrada "
             "do Caldeirão Furado."),
            ("Warner Bros. Studio Tour", "Studio Tour Drive, Leavesden, WD25 7LR",
             "Trem de Euston a Watford Junction + ônibus da Warner",
             "Salão Principal, Beco Diagonal, Expresso de Hogwarts e a maquete do castelo. Ingresso com hora "
             "marcada, que esgota semanas antes."),
        ],
    },
    {
        "id": "kids",
        "emoji": "🧒",
        "nome": "Rota Kids",
        "chamada": "Dinossauros · navio pirata · zoológico · aquário",
        "descricao": (
            "Paradas para crianças, quase todas cobertas, boas para dia de chuva. Os museus de South "
            "Kensington são grátis."
        ),
        "duracao": "2 dias em ritmo de criança",
        "paradas": [
            ("Natural History Museum", "Cromwell Road, SW7 5BD", "South Kensington (District, Circle, Piccadilly)",
             "Dinossauros, com um T-rex que se mexe, e a sala que simula um terremoto."),
            ("Science Museum", "Exhibition Road, SW7 2DD", "South Kensington (District, Circle, Piccadilly)",
             "O Wonderlab, galeria paga, tem experimentos que as próprias crianças operam."),
            ("Diana Memorial Playground", "Kensington Gardens, W2 4RU", "Queensway (Central)",
             "Parquinho com um navio pirata de madeira na areia. Adulto só entra acompanhado de criança."),
            ("Hamleys", "188–196 Regent Street, W1B 5BT", "Oxford Circus (Central, Victoria, Bakerloo)",
             "Sete andares de brinquedo, com vendedores fazendo demonstrações em cada um."),
            ("ZSL London Zoo", "Outer Circle, Regent's Park, NW1 4RY", "Camden Town (Northern)",
             "O zoológico científico mais antigo do mundo, aberto em 1828. Gorilas, tigres e pinguins."),
            ("SEA LIFE London Aquarium", "County Hall, Westminster Bridge Road, SE1 7PB", "Waterloo ou Westminster",
             "Tubarões e pinguins ao lado do London Eye; o combo com a roda-gigante sai mais barato."),
        ],
    },
]

# ---------------------------------------------------------------------------
# Estimativa de gastos (libras por pessoa por dia)
# ---------------------------------------------------------------------------
PERFIS = {
    "Econômico": {"Alimentação": 30, "Transporte": 9, "Atrações": 10, "Extras": 10},
    "Médio": {"Alimentação": 55, "Transporte": 12, "Atrações": 25, "Extras": 20},
    "Premium": {"Alimentação": 110, "Transporte": 25, "Atrações": 55, "Extras": 45},
}

CATEGORIAS = {
    "Alimentação": "refeições, cafés e lanches",
    "Transporte": "metrô, ônibus e um Uber de vez em quando",
    "Atrações": "ingressos e passeios",
    "Extras": "lembranças, imprevistos e gorjetas",
}

TARIFA_HEATHROW = 5.90  # Piccadilly Line, zona 1 ↔ Heathrow, contactless/Oyster (2026)

INGRESSOS = [
    ("Museus nacionais (British Museum, NHM, V&A, Tate, National Gallery)", "Grátis"),
    ("Tower of London", "£37 adulto"),
    ("Warner Bros. Studio Tour", "a partir de £56 adulto"),
    ("London Eye", "a partir de £29 online, varia por data"),
    ("Metrô e ônibus, zonas 1–2", "teto de £8,90 por dia"),
    ("Ônibus", "£1,75, com baldeações livres por 1 hora"),
    ("Piccadilly Line ↔ Heathrow", "£5,90 por trecho"),
    ("Refeição rápida (Pret, Leon, mercado)", "£8–14 (estimativa)"),
    ("Restaurante médio", "£25–40 por pessoa (estimativa)"),
    ("Chá da tarde em hotel de luxo", "£70–100 por pessoa (estimativa)"),
]

# ---------------------------------------------------------------------------
# Segurança
# ---------------------------------------------------------------------------
# Zonas do mapa: (nome, nível, latitude, longitude, raio em metros, observação).
# O nível é uma orientação geral para turistas, pensando na volta para o hotel à noite;
# não é estatística oficial de crime.
MAPA_SEGURANCA = [
    ("West End", "verde", 51.5122, -0.1345, 800,
     "Soho, Mayfair, Covent Garden e Piccadilly. Cheio até a saída dos teatros. O risco é furto: celular na mão "
     "na Oxford Street e em Piccadilly Circus é alvo comum."),
    ("Westminster", "verde", 51.5004, -0.1305, 550,
     "Movimentado de dia e de noite. Batedores de carteira na Westminster Bridge e o golpe dos copinhos."),
    ("South Bank", "verde", 51.5058, -0.1050, 650,
     "Beira-rio iluminada e com gente até tarde, do London Eye ao Borough Market."),
    ("City of London", "verde", 51.5140, -0.0880, 700,
     "Tranquila, mas esvazia depois das 21h e no fim de semana. Ruas desertas, não perigosas."),
    ("Kensington", "verde", 51.4985, -0.1745, 700,
     "Museus, hotéis e Knightsbridge. Um dos bairros mais calmos do centro."),
    ("Chelsea", "verde", 51.4870, -0.1675, 600,
     "Residencial e calmo. Só lota em dia de jogo em Stamford Bridge."),
    ("Notting Hill", "verde", 51.5125, -0.2020, 650,
     "Residencial e tranquilo. A exceção é o Carnaval de agosto, com multidão e furtos."),
    ("Canary Wharf", "verde", 51.5050, -0.0200, 600,
     "Área corporativa com seguranças e câmeras por todo lado. Vazia no fim de semana."),
    ("Greenwich", "verde", 51.4815, -0.0060, 650,
     "Tranquilo. À noite, fique perto do centro e da estação Cutty Sark."),
    ("Camden", "atencao", 51.5395, -0.1430, 600,
     "Divertido de dia. À noite há venda de droga e abordagem perto da estação Camden Town; fique nas ruas cheias."),
    ("King's Cross", "atencao", 51.5310, -0.1235, 550,
     "A estação e o Granary Square são movimentados; as ruas em volta esvaziam depois da meia-noite."),
    ("Shoreditch", "atencao", 51.5258, -0.0785, 600,
     "Vida noturna intensa. Furto de celular por gente de bicicleta e confusão na saída dos bares."),
    ("Hackney", "atencao", 51.5455, -0.0560, 800,
     "Bares em Dalston e na Mare Street. Fora das ruas principais, fica escuro e vazio tarde da noite."),
    ("Brixton", "atencao", 51.4620, -0.1150, 650,
     "Mercado e música ao vivo. Depois da meia-noite, prefira Uber a esperar ônibus na rua."),
]

DICAS_SEGURANCA = [
    ("Celular", "Não fique com ele na mão na beira da calçada: furto de bicicleta e moto é comum no centro"),
    ("Mochila no metrô cheio", "Na frente do corpo"),
    ("Passaporte", "No cofre do hotel; ande com uma foto dele no celular"),
    ("Batedores de carteira", "Oxford Street, Westminster Bridge, mercados e metrô lotado"),
    ("Jogo dos copinhos", "Na Westminster Bridge, é golpe com plateia combinada"),
    ("Voltando tarde", "Night Tube (sexta e sábado), ônibus noturnos com N na frente, ou Uber/Bolt"),
    ("Contactless", "Entre e saia com o mesmo cartão ou celular; o teto diário só vale assim"),
    ("Emergência", "999 para polícia, ambulância e bombeiros · 101 quando não é urgente"),
]

HEATHROW = {
    "intro": (
        "Do centro para o aeroporto, a opção barata é a Piccadilly Line, a linha azul-escura. Não confunda "
        "com a Elizabeth Line, roxa, que também vai a Heathrow por outro caminho, é mais rápida e custa mais."
    ),
    "linha": "Piccadilly Line",
    "resumo": "Zona 6 · cerca de 50 minutos do centro",
    "sentidos": [
        ("Heathrow → Londres", "Qualquer trem no sentido leste serve"),
        ("Londres → Heathrow", "Leia o destino no letreiro antes de entrar"),
    ],
    "ramais": [
        ("Destino Heathrow Terminal 5", "Para em T2&3 e T5", "Não passa no Terminal 4"),
        ("Destino Heathrow Terminal 4", "Para em T4 e depois em T2&3", "Não vai ao Terminal 5"),
    ],
    "uxbridge": "Trens com destino Uxbridge ou Rayners Lane se separam em Acton Town e não vão ao aeroporto.",
    "trem_errado": "Desça em Hatton Cross, a última estação antes dos terminais, e espere o trem certo.",
    "fatos": [
        ("Tarifa com contactless ou Oyster", "£5,90 por trecho"),
        ("Frequência", "A cada 5 a 10 minutos"),
        ("Horário", "Das 5h até perto da meia-noite"),
        ("Night Tube", "Sexta e sábado, a noite toda"),
        ("Ônibus noturno", "N9, de Aldwych até o Terminal 5"),
        ("Elizabeth Line", "Uns 35–40 min de Tottenham Court Road; confira se o trem vai a Heathrow ou a Reading"),
        ("Heathrow Express", "15 minutos de Paddington; a opção mais cara"),
    ],
}
