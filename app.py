from flask import Flask, render_template
import data

news_list = data.news_list
carousel_list = data.carousel_list
estados = data.estados


app = Flask(__name__)
# instanciar o flask e puxar o construtor

@app.route("/")
def pagina_principal():
    return render_template("index.html", noticias=news_list, carrossel=carousel_list, estados=estados)

@app.route("/notícia/<int:id>")
def show_noticia(id):
    for new in news_list:
        if int(new.get_id()) == int(id):
            return render_template("new.html", new=new)
    return render_template("new.html", noticias=news_list, estados=estados)

app.run(debug=True)