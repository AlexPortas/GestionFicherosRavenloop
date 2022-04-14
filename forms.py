from email import message
from wtforms import Form, StringField, PasswordField, validators

class LoginForm(Form):
    user = StringField('Usuario', [
        validators.Required(message='El usuario es requerido')
    ])
    pwd = PasswordField('Contraseña', [
        validators.Required(message='La contraseña es requerida')
    ])

class CreateForm(Form):
    user = StringField('Usuario', [
        validators.Required(message='El usuario es requerido')
    ])
    pwd = PasswordField('Contraseña', [
        validators.Required(message='La contraseña es requerida')
    ])