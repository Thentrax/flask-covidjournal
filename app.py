from flask import Flask, render_template
from data import News

news_list = [
    News (0, "Brasil tem 672 mortes por Covid-19 e 59.253 novos casos em 24h", "Mais de 26 milhões de pessoas já se recuperaram da doença no país, segundo dados do Ministério da Saúde; média móvel de óbitos registra tendência de queda", "O Brasil registrou, neste sábado (5), 672 mortes por Covid-19 e 59.253 novos casos diagnosticados, de acordo com os dados enviados pelos estados ao Ministério da Saúde e ao Conass (Conselho Nacional de Secretários de Saúde).\n\nCom o balanço de hoje, o país contabiliza 651.927 óbitos e 29.033.052 pessoas que já foram diagnosticadas com a doença. De acordo com o Ministério da Saúde, mais de 26 milhões de pessoas já se recuperaram da Covid-19 no país.\n\nSegundo o Conass, a taxa de letalidade do coronavírus no Brasil é de 2,2% e a taxa de mortalidade por cada 100 mil habitantes é de 310,2. A média móvel de óbitos nos últimos 7 dias é de 431, e a média móvel de novos casos é de 41.286.", 'https://img.r7.com/images/uti-hran-covid-10022022164659828?dimensions=771x420'),
    News (1, "Começa a venda de autotestes de Covid nas farmácias", "Farmácias brasileiras começaram a vender o autoteste de Covid. Com esse kit, a própria pessoa pode fazer o exame, em qualquer lugar, e saber se está infectado. Caso esteja, ela deve ir a uma unidade de saúde e fazer um exame PCR.", "Depois de receberem aprovação da Anvisa, os autotestes de covid já estão sendo comercializados pelas farmácias por meio de suas lojas online. É o caso da Drogaria São Paulo e da Drograria Pacheco.\n\nO kit – que vem com um dispositivo de teste, tampão de extração, filtro e o swab, um cotonete usado para a coleta nasal – custa R$ 69,90.\n\nEsse teste caseiro de antígeno coleta o material no fundo da boca e do nariz em busca sinais de anticorpos gerados após a infecção. O resultado sai em torno e 15 minutos. Até o momento, a Anvisa já aprovou 4 exames do tipo.\n\nJá há previsão para que esse kit esteja disponível neste semana também nas lojas físicas. A Anvisa deu autorização de comercialização apenas para farmácias e estabelecimentos de saúde.\n\nO autoteste não define um diagnóstico, seu caráter é orientativo. A indicação é, a partir do resultado positivo, procurar uma unidade de atendimento de saúde para que um profissional realize a confirmação da infecção.", 'https://catracalivre.com.br/wp-content/uploads/2022/03/autoteste-covid-farmacias-910x607.jpg'),
    News (2, "Vacinação contra a Covid-19 em Goiás: veja perguntas e respostas", "Estado recebeu 14.526.400 doses das vacinas CoronaVac, AstraZeneca/Oxford, Pfizer/BioNTech e Janssen para imunizar população goiana contra Covid-19. Goiás tem 7,1 milhões de habitantes.", "Dados colhidos pela SES-GO indicam que foram aplicadas 5.631.037 primeiras doses e 4.851.061 segundas doses em todo o estado. O reforço foi aplicado em 1.650.470 goianos. Os dados são de 14 de março de 2022.\n\nDe acordo com o Instituto Brasileiro de Geografia e Estatística (IBGE), há 7.113.540 pessoas vivendo em Goiás.\n\nSão aplicadas: CoronaVac, desenvolvida pelo laboratório parceria com o Instituto Butantan; vacina de Oxford, desenvolvida pela AstraZeneca e pela Universidade de Oxford, em parceria com a Fundação Oswaldo Cruz (Fiocruz); Pfizer/BioNTech; Janssen.", 'https://s2.glbimg.com/qdUOzx0p-IuISynCZ_0KwgquFJ4=/0x0:1700x1065/984x0/smart/filters:strip_icc()/i.s3.glbimg.com/v1/AUTH_59edd422c0c84a879bd37670ae4f538a/internal_photos/bs/2021/w/h/skUSKMQ92HUjoC8OYQOQ/vacina-goiania4.jpg'),
]

app = Flask(__name__)
# instanciar o flask e puxar o construtor

@app.route("/")
def pagina_principal():
    return render_template("index.html", noticias=news_list)

@app.route("/notícia/<int:id>")
def show_noticia(id):
    for new in news_list:
        if int(new.get_id()) == int(id):
            return render_template("new.html", new=new)
    return render_template("new.html", noticias=news_list)

app.run(debug=True)