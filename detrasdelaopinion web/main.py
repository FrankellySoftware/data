# pip install flask , flask-login , flask_mysql , gunicorn, pymongo
import platform
import json
from pymongo import MongoClient,errors
import os
import datetime
from flask import render_template, request, redirect, url_for, Flask, flash


app = Flask(__name__)

# ========== CONFIGURACION FLASK ===========
app.config['SECRET_KEY'] = "fsdgsdashedgehertjdgbdfjndf"


# ========== CONFIGURACION DE LA BBDD ===========
host = MongoClient("mongodb+srv://frankellysoftware:Leon_crack2077@cluster0.bggvz.mongodb.net/DDLO?retryWrites=true&w=majority")
db = host.get_database("DDLO")
admin = db.admin
noticias = db.noticias


# ========== DATOS GLOBALES 🌐 ===========
@app.context_processor
def datos_globales():
    datos = {
        # Esta variable se usara para enviar el tiempo a la template
        "fecha_footer": '2021 - {}'.format(datetime.datetime.utcnow().year),
        'url': request.url_root
    }
    return datos


# ========== Funciones GLOBALES 🌐 ===========
def getTituloUrl(titulo):
    list_noticias = noticias.find({})
    for li in list_noticias:
        if li["titulo_url"] == titulo:
            return [li["id"], li]


def getDocumentosBBDD():
    documentos = noticias.find(
        {}, {'_id': 0,'titulo_url': 1, 'titulo': 1, 'resumen': 1, 'imagenes': 1})

    docs = []

    for i in documentos:
        docs.append(i)
    return docs

# ========== PAGINA DE ERROR 404 ===========
@app.errorhandler(404)
def error404(e):
    return render_template("404.html")


# ==========  PAGINA DE INICIO ===========
@app.route("/")
def index():
    try:
        a = noticias.find({},limit=3)
        return render_template("index.html", relevantes = a)
    except errors.AutoReconnect:
        return "<h1>Error al conectarse con el servidor - 500</h1>"
# ========== PAGINA DE ACERCA DE NOSOTROS ===========


@app.route("/acerca-de-nosotros")
def acerca_de():
    return render_template("acerca_de.html")


# ========== PAGINA DE POST ===========
@app.route("/noticias")
def post():
    cards = getDocumentosBBDD()
    return render_template("post.html" ,cards = cards)


# ========== noticia ===========

@app.route("/noticias/<titulo_url>")
def noticia(titulo_url):

    # => retorna una Lista si exite el titulo en la base de datos, de lo contrario None
    a = getTituloUrl(titulo_url)

    if a is not None:
        """
                ==========================INFORMACION============================

                la variable 'documento' procediente del servidor, contiene la informacion de la Noticia solicitada. 
                Esta variable es de tipo Json o Dict en Python y contiene las siguentes Claves:
                
                - id
                - titulo_url
                - titulo
                - descripcion
                - video
                - img 
                - fecha
                - oculto => esto solo el backend (tipo boolean) 
        """
        documento = a[1]
        return render_template("post/noticia.html", documento=documento)

    else:
        return redirect(url_for('post'))


# ========== PAGINA DE CONTACTO ===========
@app.route("/contact")
def contacto():
    return render_template("contacto.html")


if __name__ == "__main__":
    app.run(host="10.0.0.50",debug=True)
