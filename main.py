from flask import Flask, request, render_template, session, url_for, redirect, flash

from flask_wtf import CSRFProtect

from config import DevelopmentConfig

from models import db, User
import forms

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

csrf = CSRFProtect()

@app.errorhandler(404)
def pageError(e):
    titulo='Página no encontrada'
    return render_template('error.html', titulo=titulo)

@app.before_request
def beforeRequest():
    if 'user' in session and request.endpoint in ['login', 'create']:
        return redirect(url_for('index'))

@app.route('/login', methods=['GET','POST'])
def login():
    titulo="Bienvenido"
    login_form = forms.LoginForm(request.form)
    if request.method=='POST' and login_form.validate():
        user=login_form.user.data
        pwd=login_form.pwd.data

        nuevoUsuario=User.query.filter_by(user=user).first()
        print(nuevoUsuario)
        if nuevoUsuario is not None and nuevoUsuario.verify_pwd(pwd):
            session['user'] = user
            return redirect(url_for('index'))
        else:
            message = 'Usuario o contraseña no valida'
            flash(message)

    return render_template('login.html', titulo=titulo, form=login_form)

@app.route('/logout')
def logout():
    if 'user' in session:
        session.pop('user')
    return redirect(url_for('login'))

@app.route('/create', methods = ['GET', 'POST'])
def create():
    titulo='Crear nuevo usuario'
    create_form = forms.CreateForm(request.form)
    if request.method == 'POST' and create_form.validate():
        user = User(create_form.user.data, create_form.pwd.data)
        db.session.add(user)
        db.session.commit()

        success_message ='Usuario registrado en la base de datos'
        flash(success_message)
         
    return render_template('create.html', titulo=titulo, form=create_form)

@app.route('/')
def index():
    if 'user' in session:
        user = session['user']
    else:
        return redirect(url_for('login'))
    titulo = "Inicio"
    return render_template('index.html', user=user, titulo=titulo)

if __name__ =='__main__':
    csrf.init_app(app)
    db.init_app(app)

    with app.app_context():
        db.create_all()

    app.run(port = 8118)