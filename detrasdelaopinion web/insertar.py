from pymongo import MongoClient
import datetime

host = MongoClient(host='127.0.0.1')
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



i = noticias.find({})

li = [] 
id = 0
for o in i:
    li.append(int(o['id']))

while id not in li:
    print(id)
    id += 1
else:
    print(f"aqui esta tu id {id}")



# def jsonDB(id, titulo_url, titulo, resumen, descripcion, video, imagenes, fecha, relevante, oculto):
    
#     i = noticias.find({})

#     li = [] 
#     id = 0
#     for o in i:
#         li.append(int(o['id']))

#     while id not in li:
#         id += 1
#     else:
#         print(f"aqui esta tu id {id}")

#     a = {
#         "id": id,

#         "titulo_url": titulo_url,

#         "titulo": titulo,

#         "resumen": resumen,

#         "descripcion": descripcion,

#         "video": [video],

#         "imagenes": [imagenes],

#         "fecha": fecha,

#         "relevante": relevante,

#         "oculto": oculto

#     }

#     noticias.insert_one(a)


# while True:
#     a = input('id')
#     b = input('url')
#     c = input('titulo')
#     d = input('resumen')
#     e = input('descripcion')
#     f = input('video')
#     g = input('imagenes')

#     jsonDB(int(a), b, c, d, e, f, g, datetime.datetime.now().strftime('%d/%m/%Y') , False , True)
