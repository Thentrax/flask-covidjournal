from application.model.dao.news_dao import ListaNoticia
from application.model.dao.states_dao import ListaEstados
from application import app
from flask import redirect, render_template, request
from application.model.entity.comments import Comments

states_list = ListaNoticia().lista_noticia()
estados = ListaEstados().lista_estados()

@app.route("/notícia/<int:id>",  methods=['POST', 'GET'])
def show_noticia(id):
    for state in states_list:
        for new in state.get_news_list():            
            if int(new.get_id()) == int(id):

                if request.method == "POST":
                    author = request.form.get('author')
                    text = request.form.get('text')
                    like = request.form.get('like')
                    try:
                        comment = Comments(author, text)
                        new.add_comment(comment, like)
                        return redirect(f'/notícia/{id}')
                    except :
                        comment = None

                comments = new.get_comments()
                numer_comments = len(new.get_comments())
                return render_template("new.html", new=new, comments=comments, number_comments=numer_comments)
    return render_template("new.html", noticias=states_list, estados=estados)