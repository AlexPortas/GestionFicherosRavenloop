from flask import Flask
from flask import request
from flask import render_template
from flask_wtf import CSRFProtect
from flask import make_response
from flask import session
from flask import url_for
from flask import redirect
from flask import flash
from flask import g 

from config import DevelopmentConfig

import forms
import json

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

csrf = CSRFProtect()

@app.errorhandler(404)
def pageError(e):
    titulo='Página no encontrada'
    return render_template('error.html', titulo=titulo)

@app.before_request
def beforeRequest():
   # print(request.endpoint)
    if 'user' in session:
        g.test = session['user']
    else:
        g.test = 'No se a logeado'

@app.after_request
def afterRequest(res):
    print(g.test)
    return res

@app.route('/', methods=['GET','POST'])
def login():
    if 'user' in session:
        user = session['user']
        print(user)
    titulo="Bienvenido"
    login_form = forms.LoginForm(request.form)
    if request.method=='POST' and login_form.validate():
        user=login_form.user.data
        success_message = 'Bienvenido {}'.format(user)
        flash(success_message)

        session['user'] = login_form.user.data
    return render_template('index.html', titulo=titulo, form=login_form)

@app.route('/ajax-login', methods=['POST'])
def ajax_login():
    user=request.form['user']
    response={'status':200, 'user':user, 'id':10}
    return json.dumps(response)

@app.route('/logout')
def logout():
    if 'user' in session:
        session.pop('user')
    return redirect(url_for('login'))

@app.route('/cookie')
def cookie():
    if 'user' in session:
        user = session['user']
    else:
        user = 'No hay session'
    titulo = "Cookie"
    response = make_response(render_template('cookie.html', user=user, titulo=titulo))
  #  response.set_cookie('usuario', 'Alex')
    return response

#http://localhost:8118/saludoPersonalizado?nombre=Alex
@app.route('/saludoPersonalizado')
def saludoPersonalizado():
    nombre = request.args.get('nombre', 'no pusistes')
    return 'Que pasa {} ??'.format(nombre)

@app.route('/p')
@app.route('/p/<name>')
@app.route('/p/<name>/<int:num>')
def sPersonalizado(name = '', num = ''):
    if(name==''):
        return 'No has introducido nombre. Que pasa desconocido ??'
    else:
        return 'Que pasa {} ??'.format(name)

@app.route('/user/<name>')
def user(name = ''):
    age=132
    lista=[1,32,True,'Alex']
    if(name==''):
        return 'No has introducido nombre. Que pasa desconocido ??'
    else:
        return render_template('user.html', nombre = name, age=age, lista=lista)

if __name__ =='__main__':
    csrf.init_app(app)
    app.run(port = 8118)