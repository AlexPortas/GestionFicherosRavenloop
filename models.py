from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import datetime

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'usuarios'

    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(50), unique=True)
    pwd = db.Column(db.String(255))
    is_admin = db.Column(db.Boolean, default=False)

    def __init__(self, user, pwd):
        self.user = user
        self.pwd = self.__create_password(pwd)

    def __create_password(self, pwd):
        return generate_password_hash(pwd)

    def verify_pwd(self, pwd):
        return check_password_hash(self.pwd, pwd)

class UploadedFiles(db.Model):
    __tablename__ = 'archivos_subidos'

    id = db.Column(db.Integer, primary_key=True)
    subido_por = db.Column(db.String(50))
    nombre = db.Column(db.String(255))
    fecha_subido = db.Column(db.DateTime, default=datetime.datetime.now)
    tamanho = db.Column(db.Integer)
    hash = db.Column(db.String(255))

    def __init__(self, subidoPor, nombre, tamanho, hash):
        self.subido_por = subidoPor
        self.nombre = nombre
        self.tamanho = tamanho
        self.hash = hash