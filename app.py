from flask import Flask, render_template
from data import news_list
from data import carousel_list


app = Flask(__name__)
# instanciar o flask e puxar o construtor

@app.route("/")
def pagina_principal():
    return render_template("index.html", noticias=news_list, carrossel=carousel_list)

@app.route("/notícia/<int:id>")
def show_noticia(id):
    for new in news_list:
        if int(new.get_id()) == int(id):
            return render_template("new.html", new=new)
    return render_template("new.html", noticias=news_list)

app.run(debug=True)