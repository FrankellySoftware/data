from flask_login import UserMixin
from werkzeug.security import generate_password_hash as cambiar
from werkzeug.security import check_password_hash as validar


class User(UserMixin):
    def __init__(self, id, name, email, password, is_admin=False):
        self.id = id
        self.name = name
        self.email = email
        self.password = cambiar(password)
        self.is_admin = is_admin

    def cambiar_password(self, password):
        self.password = cambiar(password)

    def validar_password(self, password):
        return validar(self.password, password)

    def __repr__(self):
        return '<Usuario {}>'.format(self.email)

users = []


def get_user(email):
    for user in users:
        if user.email == email:
            return user
    return None
git clone https://github.com/j2logo/tutorial-flask.git
git checkout tags/leccion4 -b leccion4