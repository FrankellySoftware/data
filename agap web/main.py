#pip install flask , flask-login , flask_mysql , gunicorn

import os
import datetime
from flask import render_template, request, redirect, url_for, Flask ,flash

app = Flask(__name__)

# ========== CONFIGURACION FLASK ===========
app.config['SECRET_KEY'] = "fsdgsdashedgehertjdgbdfjndf"

# ========== CONFIGURACION DE LA BBDD ===========
app.config["MYSQL_HOST"] = ''
app.config["MYSQL_USER"] = ''
app.config["MYSQL_PASSWORD"] = ''
app.config["MYSQL_DB"] = ''


# ========== DATOS GLOBALES 🌐 ===========
@app.context_processor
def datos_globales():
    datos = {
        #Esta variable se usara para envia el tiempo a la template
        "fecha_footer": datetime.datetime.utcnow(),
        '':''
    }
    return datos



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


# ========== SUB PAGINA DE ACERCA_DE (CLIENTES) ===========
@app.route("/about/clients")
def clientes():
    return render_template("clientes.html")

# ========== PAGINA DE Tienda ===========
@app.route("/store")
def tienda():
    return render_template("tienda.html")
# ========== PAGINA DE INICIO ===========
# ========== PAGINA DE INICIO ===========
# ========== PAGINA DE INICIO ===========


# ========== PAGINA DE CONTACTO ===========
@app.route("/contact")
def contacto():
    return render_template("contacto.html")








if __name__ == "__main__":
    app.run(debug=True)
