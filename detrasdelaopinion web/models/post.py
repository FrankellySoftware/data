from pymongo import MongoClient



"""
[
    {   
        id: 0,

        titulo_url: 'Adquisicion-americana',

        titulo:'Adquisicion americana',

        descripcion: 'dasasdafafas',

        video: ['http://youtube.com/video'],

        imagenes: [1,2,3,4,5,6],

        fecha: Date().utfnow(),

        oculto: flase,

    }
]
"""


class Noticia:
    def __init__(self,db):
        self.db = db

