from email import message
from wtforms import Form
from wtforms import StringField
from wtforms import PasswordField
from wtforms import validators

class LoginForm(Form):
    user = StringField('Usuario', [
        validators.Required(message='El usuario es requerido')
    ])
    pwd = PasswordField('Contraseña', [
        validators.Required(message='La contraseña es requerida')
    ])