from application.model.dao.news_dao import ListaNoticia
from application.model.dao.states_dao import ListaEstados
from application import app
from flask import render_template, redirect

states_list = ListaNoticia().lista_noticia()
carousel_list = ListaNoticia().lista_carrossel()
estados = ListaEstados().lista_estados()

@app.route("/estado/<string:sigla>",  methods=['GET'])
def state_news(sigla):
    print('alo')
    for estado in states_list:
        if estado.get_sigla() == sigla:
            return render_template("state_news.html", noticias=estado.get_news_list(), estados=estados)
    else:
        print('erro')
        return redirect("/")
