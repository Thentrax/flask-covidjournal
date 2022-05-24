from application.model.dao.news_dao import ListaNoticia
from application.model.dao.states_dao import ListaEstados
from application import app
from flask import render_template

states_list = ListaNoticia().lista_noticia()
estados = ListaEstados().lista_estados()

@app.route("/notícia/<int:id>")
def show_noticia(id):
    for state in states_list:
        for new in state.get_news_list():            
            if int(new.get_id()) == int(id):
                return render_template("new.html", new=new)
    return render_template("new.html", noticias=states_list, estados=estados)