from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def saludo():
    return 'Aquu estamos....'
    
#http://localhost:8118/saludoPersonalizado?nombre=Alex
@app.route('/saludoPersonalizado')
def saludoPersonalizado():
    nombre = request.args.get('nombre', 'no pusistes')
    return 'Que pasa {} ??'.format(nombre)

if __name__ =='__main__':
    app.run(debug  = True, port = 8118)