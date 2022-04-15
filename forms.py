from wtforms import Form, StringField, PasswordField, validators
from models import User

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

    def validate_user(form, field):
        user = field.data
        usuario = User.query.filter_by(user = user).first()
        if usuario is not None:
            raise validators.ValidationError('El usuario ya existe')
