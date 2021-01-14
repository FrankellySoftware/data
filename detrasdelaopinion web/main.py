#pip install flask , flask-login , flask_mysql , gunicorn, pymongo
import platform
from pymongo import MongoClient
import os
import datetime
from flask import render_template, request, redirect, url_for, Flask ,flash


app = Flask(__name__)

# ========== CONFIGURACION FLASK ===========
app.config['SECRET_KEY'] = "fsdgsdashedgehertjdgbdfjndf"

# ========== CONFIGURACION DE LA BBDD ===========
host = MongoClient(host='127.0.0.1')
db = host.get_database("DDLO")
admin = db.admin
noticias = db.noticias



# ========== DATOS GLOBALES 🌐 ===========
@app.context_processor
def datos_globales():
    datos = {
        #Esta variable se usara para enviar el tiempo a la template
        "fecha_footer": '2021 - {}'.format(datetime.datetime.utcnow().year),
        '':''
    }
    return datos


# ========== Funciones GLOBALES 🌐 ===========
def getTituloUrl(titulo):
    noticias.insert_many([{'toto':1},{'toto':2}])
    list_noticias = noticias.find({})
    for li in list_noticias:
        print(li)


# ========== PAGINA DE ERROR 404 ===========
@app.errorhandler(404)
def error404(e):
    return render_template("404.html")


# ==========  PAGINA DE INICIO ===========
@app.route("/")
def index():
    return render_template("index.html")

# ========== PAGINA DE ACERCA DE NOSOTROS ===========
@app.route("/about")
def acerca_de():
    return render_template("acerca_de.html")


# ========== PAGINA DE POST ===========
@app.route("/posts")
def post():
    return render_template("post.html")

# ========== noticia ===========
@app.route("/posts/<titulo_url>")
def noticia(titulo_url):
    getTituloUrl("sasda")


    return render_template("post/noticia.html")



# ========== PAGINA DE CONTACTO ===========
@app.route("/contact")
def contacto():
    return render_template("contacto.html")








if __name__ == "__main__":
    app.run(debug=True)

