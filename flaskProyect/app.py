#Importaciones importante
from flask import Flask

app = Flask(__name__)

#Ruta simple
@app.route('/')
def home(): #para que inicie la interfaz home
    return 'Hola mundo FLASK'

#Ruta con parametros
@app.route('/saludo/<nombre>')
def saludar(nombre): # int:nombre para castearlo pr default es string
    return 'Hola, ' + nombre
#RUTA TRY-CATH
@app.errorhandler(404) #errorhandler con el n[umero de error]
def paginaNoE(e): #pagina No Encontrada 
    print(e)
    return 'Ha ocurrido un error: !!!'

#Ruta doble
@app.route('/usuario')
@app.route('/usuaria')
def doubleroute(): #har[a] que las dos rutas de arruba lleven a lo mismo
    return 'Soy el mismo recurso del servidor'
#ruta post forzada
@app.route('/formulario',methods=['POST'])
def formulario():
    return 'Soy un formulario'


if __name__ == '__main__':
    app .run(port = 3000, debug = True)
    
