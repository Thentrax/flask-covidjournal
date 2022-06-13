from application.model.dao.news_dao import ListaNoticia
from application.model.dao.states_dao import ListaEstados
from application import app
from flask import render_template

all_news = ListaNoticia().listar_por_likes()
carousel_list = ListaNoticia().lista_carrossel()
estados = ListaEstados().lista_estados()


@app.route("/")
def pagina_principal():
    return render_template("index.html", noticias=all_news, carrossel=carousel_list, estados=estados)