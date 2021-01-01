from flask import Flask, render_template, url_for, redirect, request
import json
from controllers.funciones import add

########### lectura de archivos ############

with open("./models/json/products.json") as product:
    datos = json.load(product)
    product.close()

with open("./models/json/page_info.json") as info:
    informacion = json.load(info)
    info.close()

########### Global Vars #################

titulo = informacion["title"]
icono = informacion["icon"]
logo = informacion["logon"]
meta_desc = informacion["meta-desc"]
meta_keys = informacion["meta-keys"]

info_page = [titulo, icono, logo, meta_desc, meta_keys]


web = Flask(__name__)
web.secret_key = "asd345rewq9901"


######## inicio #########

@web.route("/")
def index():

    return render_template("index.html", info_page=info_page)


########### Pruebas ##########


########### Errores ##########


@web.errorhandler(404)
def e404(e):
    return render_template("hiddens/404.html", info_page=info_page)

############# Productos ################


@web.route("/productos")
def productos():
    lista = []
    ind = list(datos)
    for i in ind:
        lista.append(add(i, datos[i]))

    return render_template("productos.html", info_page=info_page, lista=lista)


@web.route("/productos/<id>")
def producto(id):
    for i in datos:
        i = int(i)
        if int(id) == i:
            data = datos[id]
            nombre = data[0]
            precio = data[1]
            img = data[2]
            descripcion = data[3]
            return render_template("hiddens/producto.html", info_page=info_page, id=id, nombre=nombre, precio=precio, img=img, descripcion=descripcion)


############## Compra ##############

@web.route("/buy")
def buy():
    return redirect(url_for("productos"))


@web.route("/buy/<id>")
def compra(id):

    return render_template("hiddens/buy-page.html", info_page=info_page)


################# info #################

@web.route("/contacto")
def contacto():
    return render_template('contacto.html', info_page=info_page)


@web.route("/quienes-somos")
def quienes_somos():
    return render_template('quienes-somos.html', info_page=info_page)
    


if __name__ == "__main__":
    web.run(port=5000, debug=True)
