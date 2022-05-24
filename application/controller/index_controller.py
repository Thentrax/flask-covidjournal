from application.model.dao.news_dao import ListaNoticia
from application.model.dao.states_dao import ListaEstados
from application import app
from flask import render_template

states_list = ListaNoticia().lista_noticia()
carousel_list = ListaNoticia().lista_carrossel()
estados = ListaEstados().lista_estados()


@app.route("/")
def pagina_principal():
    return render_template("index.html", noticias=states_list, carrossel=carousel_list, estados=estados)