from pymongo import MongoClient
import datetime

host = MongoClient("mongodb+srv://frankellysoftware:Leon_crack2077@cluster0.bggvz.mongodb.net/DDLO?retryWrites=true&w=majority")
db = host.get_database("DDLO")
admin = db.admin
noticias = db.noticias


"""
[
    {   
        "id": 0,

        "titulo_url": "Adquisicion-americana",

        "titulo":"'Adquisicion americana'",

        "resumen":"aqui un pequeno resumen de 100 caracteres",

        "descripcion": "dasa<a>sdaf</a>afas",

        "video": ["https://youtube.com/video"],

        "imagenes": [1,2,3,4,5,6],

        "fecha": "",

        "relevante": true,

        "oculto": false

    }
]
"""

#crear mi propia funcion en flask
# @app.context_processor
# def suma1():
#     def suma(n1, n2):
#         return n1+n2
#     return dict(suma=suma)



def jsonDB(titulo, resumen, descripcion, video, imagenes, fecha, relevante, oculto):
    
    i = noticias.find({})
    li = [] 
    id = 0
    for o in i:
        li.append(int(o['id']))

    while id in li:
        id += 1

    titulo_url = titulo.replace(" "  ,  "-")

    a = {
        "id": id,

        "titulo_url": titulo_url.lower(),

        "titulo": titulo.capitalize(),

        "resumen": resumen,

        "descripcion": descripcion,

        "video": [video],

        "imagenes": [imagenes],

        "fecha": fecha,

        "relevante": relevante,

        "oculto": oculto

    }

    noticias.insert_one(a)


while True:
    c = input('titulo: ')
    d = input('resumen: ')
    e = input('descripcion: ')
    f = input('video: ')
    g = input('imagenes: ')

    jsonDB( c, d, e, f, g, datetime.datetime.now().strftime('%d/%m/%Y') , False , True)
