from flask import Flask
from flask import request
from flask import render_template
import forms

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def login():
    titulo="Bienvenido"
    login_form = forms.LoginForm()
    return render_template('index.html', titulo=titulo, form=login_form)

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
    app.run(debug  = True, port = 8118)