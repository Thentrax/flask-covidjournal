from application.model.entity.news import News
from application.model.dao.states_dao import ListaEstados

estados = ListaEstados().lista_estados()

df_list = [
    News ("Brasil tem 672 mortes por Covid-19 e 59.253 novos casos em 24h", "Mais de 26 milhões de pessoas já se recuperaram da doença no país, segundo dados do Ministério da Saúde; média móvel de óbitos registra tendência de queda", "O Brasil registrou, neste sábado (5), 672 mortes por Covid-19 e 59.253 novos casos diagnosticados, de acordo com os dados enviados pelos estados ao Ministério da Saúde e ao Conass (Conselho Nacional de Secretários de Saúde).\n\nCom o balanço de hoje, o país contabiliza 651.927 óbitos e 29.033.052 pessoas que já foram diagnosticadas com a doença. De acordo com o Ministério da Saúde, mais de 26 milhões de pessoas já se recuperaram da Covid-19 no país.\n\nSegundo o Conass, a taxa de letalidade do coronavírus no Brasil é de 2,2% e a taxa de mortalidade por cada 100 mil habitantes é de 310,2. A média móvel de óbitos nos últimos 7 dias é de 431, e a média móvel de novos casos é de 41.286.", 'https://img.r7.com/images/uti-hran-covid-10022022164659828?dimensions=771x420', estados[6], 20)
]

go_list = [
    News ("Vacinação contra a Covid-19 em Goiás: veja perguntas e respostas", "Estado recebeu 14.526.400 doses das vacinas CoronaVac, AstraZeneca/Oxford, Pfizer/BioNTech e Janssen para imunizar população goiana contra Covid-19. Goiás tem 7,1 milhões de habitantes.", "Dados colhidos pela SES-GO indicam que foram aplicadas 5.631.037 primeiras doses e 4.851.061 segundas doses em todo o estado. O reforço foi aplicado em 1.650.470 goianos. Os dados são de 14 de março de 2022.\n\nDe acordo com o Instituto Brasileiro de Geografia e Estatística (IBGE), há 7.113.540 pessoas vivendo em Goiás.\n\nSão aplicadas: CoronaVac, desenvolvida pelo laboratório parceria com o Instituto Butantan; vacina de Oxford, desenvolvida pela AstraZeneca e pela Universidade de Oxford, em parceria com a Fundação Oswaldo Cruz (Fiocruz); Pfizer/BioNTech; Janssen.", 'https://s2.glbimg.com/qdUOzx0p-IuISynCZ_0KwgquFJ4=/0x0:1700x1065/984x0/smart/filters:strip_icc()/i.s3.glbimg.com/v1/AUTH_59edd422c0c84a879bd37670ae4f538a/internal_photos/bs/2021/w/h/skUSKMQ92HUjoC8OYQOQ/vacina-goiania4.jpg', estados[8], 12)
]

mg_list = [
    News ("Ministro da Saúde diz em BH que pandemia deve ser rebaixada para endemia até o início de abril", "Endemia é status conferido a doenças recorrentes, para a qual a população e serviços de saúde já estão preparados. Segundo Queiroga, a pandemia está sob controle em vários estados e a população está 'fortemente vacinada'.", 'O ministro da Saúde Marcelo Queiroga disse nesta sexta-feira (18), em Belo Horizonte que a pandemia pode ser rebaixada para endemia muito em breve. Ele participou da abertura da oficina do programa Previne Brasil, da Atenção Primária, na Cidade Administrativa, sede do governo do estado.', 'https://s2.glbimg.com/EEm--En-YyXn4QBeu6JtDKkKmh0=/0x0:1920x1080/984x0/smart/filters:strip_icc()/i.s3.glbimg.com/v1/AUTH_59edd422c0c84a879bd37670ae4f538a/internal_photos/bs/2022/v/i/ejvbELQqiQAOc8zDDysw/coletiva-ministro-saude-iana-18-mar-2022-frame-15298.jpeg',estados[12], 2)
]

rj_list = [
    News ("Começa a venda de autotestes de Covid nas farmácias", "Farmácias brasileiras começaram a vender o autoteste de Covid. Com esse kit, a própria pessoa pode fazer o exame, em qualquer lugar, e saber se está infectado. Caso esteja, ela deve ir a uma unidade de saúde e fazer um exame PCR.", "Depois de receberem aprovação da Anvisa, os autotestes de covid já estão sendo comercializados pelas farmácias por meio de suas lojas online. É o caso da Drogaria São Paulo e da Drograria Pacheco.\n\nO kit – que vem com um dispositivo de teste, tampão de extração, filtro e o swab, um cotonete usado para a coleta nasal – custa R$ 69,90.\n\nEsse teste caseiro de antígeno coleta o material no fundo da boca e do nariz em busca sinais de anticorpos gerados após a infecção. O resultado sai em torno e 15 minutos. Até o momento, a Anvisa já aprovou 4 exames do tipo.\n\nJá há previsão para que esse kit esteja disponível neste semana também nas lojas físicas. A Anvisa deu autorização de comercialização apenas para farmácias e estabelecimentos de saúde.\n\nO autoteste não define um diagnóstico, seu caráter é orientativo. A indicação é, a partir do resultado positivo, procurar uma unidade de atendimento de saúde para que um profissional realize a confirmação da infecção.", 'https://catracalivre.com.br/wp-content/uploads/2022/03/autoteste-covid-farmacias-910x607.jpg', estados[18], 8),
    News ("Durante a pandemia de Covid-19, violência no Rio fechou uma unidade de saúde a cada dois dias", "Por causa da violência, vários profissionais da saúde acabam perdendo suas vidas de várias maneiras possíveis", 'Kelly Cristina de Sá Lacerda trabalhava como agente comunitária de saúde numa clínica da família no bairro de Senador Camará, na Zona Oeste do Rio, onde morava. Atuava também como líder religiosa, com ações voltadas ao atendimento da população — sobretudo crianças e adolescentes da região, alguns deles dependentes químicos. Certo dia, estava a caminho do trabalho quando, ainda perto de casa, foi atingida por um tiro na barriga. Mãe de dois filhos, Kelly, cuja missão era zelar pela vida da comunidade garantindo que seus vizinhos estivessem sempre com saúde, teve a própria vida ceifada aos 40 anos por algo que, no Rio de Janeiro, parece já ser compreendido como um fenômeno da natureza: a violência.', 'https://extra.globo.com/incoming/25449595-7ce-a9e/w640h360-PROP/98285401_ririo-de-janeiro-rj-25-03-2022-impacto-da-violencia-na-rede-de-saude-cms-aloysio-ama.jpg', estados[18], 10)
]


sp_list = [
    News ("SP promove o “Domingão da Vacinação” para imunização contra Covid-19 e a gripe", "Imunização contra o novo coronavírus será aplicada em crianças, adultos e idosos e a vacina contra a Influenza em quem tiver mais de 80 anos", 'O Governo de SP, em parceria com os 645 municípios, promove no neste dia 27 o “Domingão da Vacinação” para a imunização de crianças, adultos e idosos contra Covid-19. Além disso, os idosos acima de 80 anos poderão se vacinar contra a gripe.\n\nA iniciativa busca ampliar a imunização das crianças de 5 a 11 anos de idade, principalmente com relação a segunda dose contra a COVID-19. No estado 76% do público infantil já tomou a primeira dose, porém apenas 36% receberam as duas doses e completou a imunização, sendo que cerca de 800 mil crianças já poderiam ter recebido a segunda dose. Uma pesquisa da Fundação Seade apontou que 34% dos pais e responsáveis afirmaram que não levaram os filhos para vacinar por falta de tempo.', 'https://prefeitura.rio/wp-content/uploads/2021/02/Idalicio-Vacina-5.jpg',estados[24], 35),
    News ("Covid-19: após ficar 24 horas sem mortes, SP registra mais seis óbitos e 590 casos da doença", "Ao todo, o Estado já contabilizou 14.329 mortes e 1.037.963 casos confirmados de infecção pelo coronavírus, desde o início da pandemia, há dois anos", 'Após o domingo (27) sem registros de mortes por covid-19, o Espírito Santo voltou a contabilizar óbitos provocados pela doença, nesta segunda-feira (28). De acordo com o Painel Covid-19, da Secretaria de Estado da Saúde (Sesa), foram registradas seis mortes entre domingo e segunda-feira, totalizando 14.329 desde o início da pandemia, há dois anos.\n\As seis mortes mais recentes contabilizadas no Painel Covid-19, no entanto, não necessariamente aconteceram nas últimas 24 horas. Após fins de semanas e feriados, é comum que os números estejam maiores, em relação aos dias anteriores, pelo fato de haver um represamento dos dados processados pela Sesa.', 'https://img.r7.com/images/folha-vitoria-28032022193424406?dimensions=771x420',estados[24], 40)
]


news_list = []
news_list.extend(df_list)
news_list.extend(go_list)
news_list.extend(mg_list)
news_list.extend(rj_list)
news_list.extend(sp_list)

for new in news_list:
    elements = len(news_list)-1
    ordered = False
    while not ordered:
        ordered = True    
        for new in range(elements):
            if news_list[new].get_likes() < news_list[new+1].get_likes():
                aux = news_list[new]
                news_list[new] = news_list[new+1]
                news_list[new+1] = aux
                ordered = False

estados[6].set_news_list(df_list)
estados[8].set_news_list(go_list)
estados[12].set_news_list(mg_list)
estados[18].set_news_list(rj_list)
estados[24].set_news_list(sp_list)

states_list =[            
            estados[6],
            estados[8],
            estados[12],
            estados[18],
            estados[24]
        ]


class ListaNoticia:
    def lista_noticia(self):
        return states_list
    
    def lista_carrossel(self):
        carousel_list = [
            states_list[0].get_news_list()[0],
            states_list[1].get_news_list()[0],
            states_list[2].get_news_list()[0]
        ]
        return carousel_list