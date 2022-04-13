from distutils.debug import DEBUG
import os

class Config(object):
    SECRET_KEY = 'Esto_es_un_secreto'

class DevelopmentConfig(Config):
    DEBUG = True