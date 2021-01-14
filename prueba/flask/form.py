from wtforms import Form
from wtforms import StringField,TextField
from wtforms.fields.html5 import EmailField

class CommentForm(Form):
    userName = StringField("username")
    email = EmailField("Correo Electronico")
    comment = TextField('Comentario')