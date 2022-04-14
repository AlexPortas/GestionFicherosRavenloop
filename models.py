from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

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