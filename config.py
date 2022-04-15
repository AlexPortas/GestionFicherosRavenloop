from distutils.debug import DEBUG
import os

class Config(object):
    SECRET_KEY = 'Esto_es_un_secreto'

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:@localhost/GestionFicheros'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = './Archivos'