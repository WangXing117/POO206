#Importaciones importante
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home(): #para que inicie la interfaz home
    return 'Hola mundo FLASK'

if __name__ == '__main__':
    app .run(port = 3000, debug = True)
    
