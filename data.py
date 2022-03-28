class News:

    def __init__(self, id, tittle, headline, text, image, state):
        self.__id = id
        self.__tittle = tittle
        self.__headline = headline
        self.__text = text
        self.__image = image
        self.__state = state
    
    def get_id(self):
        return self.__id
    
    def get_tittle(self):
        return self.__tittle
    
    def get_headline(self):
        return self.__headline

    def get_text(self):
        return self.__text
    
    def get_image(self):
        return self.__image

    def get_state(self):
        return self.__state

carousel_list = [
    News (0, "Brasil tem 672 mortes por Covid-19 e 59.253 novos casos em 24h", "Mais de 26 milhões de pessoas já se recuperaram da doença no país, segundo dados do Ministério da Saúde; média móvel de óbitos registra tendência de queda", "O Brasil registrou, neste sábado (5), 672 mortes por Covid-19 e 59.253 novos casos diagnosticados, de acordo com os dados enviados pelos estados ao Ministério da Saúde e ao Conass (Conselho Nacional de Secretários de Saúde).\n\nCom o balanço de hoje, o país contabiliza 651.927 óbitos e 29.033.052 pessoas que já foram diagnosticadas com a doença. De acordo com o Ministério da Saúde, mais de 26 milhões de pessoas já se recuperaram da Covid-19 no país.\n\nSegundo o Conass, a taxa de letalidade do coronavírus no Brasil é de 2,2% e a taxa de mortalidade por cada 100 mil habitantes é de 310,2. A média móvel de óbitos nos últimos 7 dias é de 431, e a média móvel de novos casos é de 41.286.", 'https://img.r7.com/images/uti-hran-covid-10022022164659828?dimensions=771x420', 'DF'),
    News (1, "Começa a venda de autotestes de Covid nas farmácias", "Farmácias brasileiras começaram a vender o autoteste de Covid. Com esse kit, a própria pessoa pode fazer o exame, em qualquer lugar, e saber se está infectado. Caso esteja, ela deve ir a uma unidade de saúde e fazer um exame PCR.", "Depois de receberem aprovação da Anvisa, os autotestes de covid já estão sendo comercializados pelas farmácias por meio de suas lojas online. É o caso da Drogaria São Paulo e da Drograria Pacheco.\n\nO kit – que vem com um dispositivo de teste, tampão de extração, filtro e o swab, um cotonete usado para a coleta nasal – custa R$ 69,90.\n\nEsse teste caseiro de antígeno coleta o material no fundo da boca e do nariz em busca sinais de anticorpos gerados após a infecção. O resultado sai em torno e 15 minutos. Até o momento, a Anvisa já aprovou 4 exames do tipo.\n\nJá há previsão para que esse kit esteja disponível neste semana também nas lojas físicas. A Anvisa deu autorização de comercialização apenas para farmácias e estabelecimentos de saúde.\n\nO autoteste não define um diagnóstico, seu caráter é orientativo. A indicação é, a partir do resultado positivo, procurar uma unidade de atendimento de saúde para que um profissional realize a confirmação da infecção.", 'https://catracalivre.com.br/wp-content/uploads/2022/03/autoteste-covid-farmacias-910x607.jpg', 'RJ'),
    News (2, "Vacinação contra a Covid-19 em Goiás: veja perguntas e respostas", "Estado recebeu 14.526.400 doses das vacinas CoronaVac, AstraZeneca/Oxford, Pfizer/BioNTech e Janssen para imunizar população goiana contra Covid-19. Goiás tem 7,1 milhões de habitantes.", "Dados colhidos pela SES-GO indicam que foram aplicadas 5.631.037 primeiras doses e 4.851.061 segundas doses em todo o estado. O reforço foi aplicado em 1.650.470 goianos. Os dados são de 14 de março de 2022.\n\nDe acordo com o Instituto Brasileiro de Geografia e Estatística (IBGE), há 7.113.540 pessoas vivendo em Goiás.\n\nSão aplicadas: CoronaVac, desenvolvida pelo laboratório parceria com o Instituto Butantan; vacina de Oxford, desenvolvida pela AstraZeneca e pela Universidade de Oxford, em parceria com a Fundação Oswaldo Cruz (Fiocruz); Pfizer/BioNTech; Janssen.", 'https://s2.glbimg.com/qdUOzx0p-IuISynCZ_0KwgquFJ4=/0x0:1700x1065/984x0/smart/filters:strip_icc()/i.s3.glbimg.com/v1/AUTH_59edd422c0c84a879bd37670ae4f538a/internal_photos/bs/2021/w/h/skUSKMQ92HUjoC8OYQOQ/vacina-goiania4.jpg', 'GO'),
]

news_list = [
    News (0, "Brasil tem 672 mortes por Covid-19 e 59.253 novos casos em 24h", "Mais de 26 milhões de pessoas já se recuperaram da doença no país, segundo dados do Ministério da Saúde; média móvel de óbitos registra tendência de queda", "O Brasil registrou, neste sábado (5), 672 mortes por Covid-19 e 59.253 novos casos diagnosticados, de acordo com os dados enviados pelos estados ao Ministério da Saúde e ao Conass (Conselho Nacional de Secretários de Saúde).\n\nCom o balanço de hoje, o país contabiliza 651.927 óbitos e 29.033.052 pessoas que já foram diagnosticadas com a doença. De acordo com o Ministério da Saúde, mais de 26 milhões de pessoas já se recuperaram da Covid-19 no país.\n\nSegundo o Conass, a taxa de letalidade do coronavírus no Brasil é de 2,2% e a taxa de mortalidade por cada 100 mil habitantes é de 310,2. A média móvel de óbitos nos últimos 7 dias é de 431, e a média móvel de novos casos é de 41.286.", 'https://img.r7.com/images/uti-hran-covid-10022022164659828?dimensions=771x420', 'DF'),
    News (1, "Começa a venda de autotestes de Covid nas farmácias", "Farmácias brasileiras começaram a vender o autoteste de Covid. Com esse kit, a própria pessoa pode fazer o exame, em qualquer lugar, e saber se está infectado. Caso esteja, ela deve ir a uma unidade de saúde e fazer um exame PCR.", "Depois de receberem aprovação da Anvisa, os autotestes de covid já estão sendo comercializados pelas farmácias por meio de suas lojas online. É o caso da Drogaria São Paulo e da Drograria Pacheco.\n\nO kit – que vem com um dispositivo de teste, tampão de extração, filtro e o swab, um cotonete usado para a coleta nasal – custa R$ 69,90.\n\nEsse teste caseiro de antígeno coleta o material no fundo da boca e do nariz em busca sinais de anticorpos gerados após a infecção. O resultado sai em torno e 15 minutos. Até o momento, a Anvisa já aprovou 4 exames do tipo.\n\nJá há previsão para que esse kit esteja disponível neste semana também nas lojas físicas. A Anvisa deu autorização de comercialização apenas para farmácias e estabelecimentos de saúde.\n\nO autoteste não define um diagnóstico, seu caráter é orientativo. A indicação é, a partir do resultado positivo, procurar uma unidade de atendimento de saúde para que um profissional realize a confirmação da infecção.", 'https://catracalivre.com.br/wp-content/uploads/2022/03/autoteste-covid-farmacias-910x607.jpg', 'RJ'),
    News (2, "Vacinação contra a Covid-19 em Goiás: veja perguntas e respostas", "Estado recebeu 14.526.400 doses das vacinas CoronaVac, AstraZeneca/Oxford, Pfizer/BioNTech e Janssen para imunizar população goiana contra Covid-19. Goiás tem 7,1 milhões de habitantes.", "Dados colhidos pela SES-GO indicam que foram aplicadas 5.631.037 primeiras doses e 4.851.061 segundas doses em todo o estado. O reforço foi aplicado em 1.650.470 goianos. Os dados são de 14 de março de 2022.\n\nDe acordo com o Instituto Brasileiro de Geografia e Estatística (IBGE), há 7.113.540 pessoas vivendo em Goiás.\n\nSão aplicadas: CoronaVac, desenvolvida pelo laboratório parceria com o Instituto Butantan; vacina de Oxford, desenvolvida pela AstraZeneca e pela Universidade de Oxford, em parceria com a Fundação Oswaldo Cruz (Fiocruz); Pfizer/BioNTech; Janssen.", 'https://s2.glbimg.com/qdUOzx0p-IuISynCZ_0KwgquFJ4=/0x0:1700x1065/984x0/smart/filters:strip_icc()/i.s3.glbimg.com/v1/AUTH_59edd422c0c84a879bd37670ae4f538a/internal_photos/bs/2021/w/h/skUSKMQ92HUjoC8OYQOQ/vacina-goiania4.jpg', 'GO'),
    News (3, "SP promove o “Domingão da Vacinação” para imunização contra Covid-19 e a gripe", "Imunização contra o novo coronavírus será aplicada em crianças, adultos e idosos e a vacina contra a Influenza em quem tiver mais de 80 anos", 'O Governo de SP, em parceria com os 645 municípios, promove no neste dia 27 o “Domingão da Vacinação” para a imunização de crianças, adultos e idosos contra Covid-19. Além disso, os idosos acima de 80 anos poderão se vacinar contra a gripe.\n\nA iniciativa busca ampliar a imunização das crianças de 5 a 11 anos de idade, principalmente com relação a segunda dose contra a COVID-19. No estado 76% do público infantil já tomou a primeira dose, porém apenas 36% receberam as duas doses e completou a imunização, sendo que cerca de 800 mil crianças já poderiam ter recebido a segunda dose. Uma pesquisa da Fundação Seade apontou que 34% dos pais e responsáveis afirmaram que não levaram os filhos para vacinar por falta de tempo.', 'https://prefeitura.rio/wp-content/uploads/2021/02/Idalicio-Vacina-5.jpg','SP'),
    News (4, "", "", '', '',''),
    News (5, "", "", '', '',''),

]

    # News (0, "", "", '', '',''),

class Estados:

    def __init__(self, sigla, nome, flag):
        self.__sigla  = sigla
        self.__nome = nome
        self.__flag = flag

    def get_sigla(self):
        return self.__sigla
    
    def get_nome(self):
        return self.__nome

    def get_flag(self):
        return self.__flag

estados = [
    Estados ('AC','Acre','http://www.educadores.diaadia.pr.gov.br/modules/galeria/uploads/11/thumb_1409852740bandeiraacre.png'),
    Estados ('AL','Alagoas','http://www.educadores.diaadia.pr.gov.br/modules/galeria/uploads/11/thumb_1409852743Bandeira_de_Alagoas.svg.png'),
    Estados ('AP','Amapá','http://www.educadores.diaadia.pr.gov.br/modules/galeria/uploads/11/thumb_1409852744Bandeira_do_Amap.svg.png'),
    Estados ('AM','Amazonas','http://www.educadores.diaadia.pr.gov.br/modules/galeria/uploads/11/thumb_1409852744Bandeira_do_Amazonas.svg.png'),
    Estados ('BA','Bahia','http://www.educadores.diaadia.pr.gov.br/modules/galeria/uploads/11/thumb_1409852741bandeirabahia.png'),
    Estados ('CE','Ceará','http://www.educadores.diaadia.pr.gov.br/modules/galeria/uploads/11/thumb_1409852741bandeiraceara.png'),
    Estados ('DF','Distrito Federal','http://www.educadores.diaadia.pr.gov.br/modules/galeria/uploads/11/thumb_1409852741bandeiradistritofederal.png'),
    Estados ('ES','Espírito Santo','http://www.educadores.diaadia.pr.gov.br/modules/galeria/uploads/11/thumb_1409852741bandeiraespiritosanto.png'),
    Estados ('GO','Goiás','http://www.educadores.diaadia.pr.gov.br/modules/galeria/uploads/11/thumb_1409852742bandeiragoias.png'),
    Estados ('MA','Maranhão','http://www.educadores.diaadia.pr.gov.br/modules/galeria/uploads/11/thumb_1409852741bandeiradomaranhao.jpg'),
    Estados ('MT','Mato Grosso','http://www.educadores.diaadia.pr.gov.br/modules/galeria/uploads/11/thumb_1409852742bandeiramatogrosso.png'),
    Estados ('MS','Mato Grosso do Sul','http://www.educadores.diaadia.pr.gov.br/modules/galeria/uploads/11/thumb_1409852744bandeira_Mato_Grosso_Sul.png'),
    Estados ('MG','Minas Gerais','http://www.educadores.diaadia.pr.gov.br/modules/galeria/uploads/11/thumb_1409852743Bandeira_de_Minas_Gerais.svg.png'),
    Estados ('PA','Pará','http://www.educadores.diaadia.pr.gov.br/modules/galeria/uploads/11/thumb_1409852744Bandeira_do_Par.svg.png'),
    Estados ('PB','Paraíba','http://www.educadores.diaadia.pr.gov.br/modules/galeria/uploads/11/thumb_1409852742bandeiraparaiba.png'),
    Estados ('PR','Paraná','http://www.educadores.diaadia.pr.gov.br/modules/galeria/uploads/11/thumb_1409852742bandeiraparana.png'),
    Estados ('PE','Pernambuco','http://www.educadores.diaadia.pr.gov.br/modules/galeria/uploads/11/thumb_1409852741BandeiradePernambuco.png'),
    Estados ('PI','Piauí','http://www.educadores.diaadia.pr.gov.br/modules/galeria/uploads/11/thumb_1409852742bandeirapiaui.png'),
    Estados ('RJ','Rio de Janeiro','http://www.educadores.diaadia.pr.gov.br/modules/galeria/uploads/11/thumb_1409852742bandeirariodejaneiro.png'),
    Estados ('RN','Rio Grande do Norte','http://www.educadores.diaadia.pr.gov.br/modules/galeria/uploads/11/thumb_1409852742bandeirariograndedonorte.png'),
    Estados ('RS','Rio Grande do Sul','http://www.educadores.diaadia.pr.gov.br/modules/galeria/uploads/11/thumb_1409852743bandeirariograndedosul.png'),
    Estados ('RO','Rondônia','http://www.educadores.diaadia.pr.gov.br/modules/galeria/uploads/11/thumb_1409852743bandeirarondonia.png'),
    Estados ('RR','Roraima','http://www.educadores.diaadia.pr.gov.br/modules/galeria/uploads/11/thumb_1409852743bandeiraroraima.png'),
    Estados ('SC','Santa Catarina','http://www.educadores.diaadia.pr.gov.br/modules/galeria/uploads/11/thumb_1409852743bandeirasantacatarina.png'),
    Estados ('SP','São Paulo','http://www.educadores.diaadia.pr.gov.br/modules/galeria/uploads/11/thumb_1409852744Bandeira_do_estado_de_S_Paulo.svg.png'),
    Estados ('SE','Sergipe','http://www.educadores.diaadia.pr.gov.br/modules/galeria/uploads/11/thumb_1409852743bandeirasergipe.png'),
    Estados ('TO','Tocantins','http://www.educadores.diaadia.pr.gov.br/modules/galeria/uploads/11/thumb_1409852743bandeiratocantins.png')
]