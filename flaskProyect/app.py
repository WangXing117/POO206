#Importaciones importante
from flask import Flask, jsonify, render_template, request, flash, url_for, redirect
from conexion_sqlserver import obtenerConexion
from flask_mysqldb import MySQL
import MySQLdb
import pyodbc

app = Flask(__name__)
app.secret_key = 'mysecretkey'

# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = ''
# app.config['MYSQL_DB'] = 'Flaskpoo'
# app.config['MYSQL_PORT'] = 3306 #3306 ES EL PUERTO POR DEFECTO

# mysql = MySQL(app)
# @app.route('/dbcheck')
# def DB_Check():
    # try:
    #     cursor = mysql.connection.cursor()
    #     cursor.excute('Select 1') #Esto devuleve un 1 para ver q si alcance la base de datos
    #     return jsonify({
    #         'status':'ok',
    #         'message':'!! Conectado con exito !!',
    #     }), 200
    # except MySQLdb.MySQLError as e:
    #     return jsonify({
    #         'status':'Error',
    #         'message':str(e),
    #     }), 500
    
############
#Ruta simple

@app.route('/')
def home(): #para que inicie la interfaz formulario por default
    return render_template('formulario.html')

@app.route('/guardarAlbum',methods=['POST'])
def guardar():
    #obtener los datos a insertar
    titulo = request.form.get('txtTitulo','').strip() #si hay espacios a la izq o der strip los quita
    artista = request.form.get('txtArtista','').strip() #si hay espacios a la izq o der strip los quita
    anio = request.form.get('txtAno','').strip() #si hay espacios a la izq o der strip los quita
    
    #intentamos ejecutar el insert
    try:
        conn = obtenerConexion()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO Album(Titulo,Artista,Ano_Publicacion) VALUES (?,?,?)',(titulo,artista,anio))
        conn.commit() #confirmacion del cambio
        flash('Album guardado correctamente')
        return redirect(url_for('home'))
    except Exception as e:
        conn.rollback() #revierte cualquier cambio
        flash('Album guardado correctamente')
        return redirect(url_for('home'))
    finally:
        conn.close() #cierra la conexion
        
@app.route('/consulta')
def consulta(): #para que inicie la interfaz consulta
    return render_template('consulta.html')

# #Ruta con parametros
# @app.route('/saludo/<nombre>')
# def saludar(nombre): # int:nombre para castearlo pr default es string
#     return 'Hola, ' + nombre
#RUTA TRY-CATH
@app.errorhandler(404) #errorhandler con el n[umero de error]
def paginaNoE(e): #pagina No Encontrada 
    print(e)
    return 'Ha ocurrido un error: !!!'

@app.errorhandler(405) #errorhandler con el n[umero de error]
def paginaNoEr(e): #pagina No Encontrada 
    print(e)
    return 'Ha ocurrido un error: !!!'

# #Ruta doble
# @app.route('/usuario')
# @app.route('/usuaria')
# def doubleroute(): #har[a] que las dos rutas de arruba lleven a lo mismo
#     return 'Soy el mismo recurso del servidor'
# #ruta post forzada
# @app.route('/formulario',methods=['POST'])
# def formulario():
#     return 'Soy un formulario'

    
@app.route('/dbcheck')
def DB_Check():
    try:
        conn = obtenerConexion()
        cursor = conn.cursor()
        cursor.execute('Select 1')
        print('!!!!!!!!!!!!! conexion exitosa !!!!!!!!!!!!!!!!!!!!!!!!!!1')
        return jsonify({
           'status':'ok',
             'message':'!! Conectado con exito !!',
         }), 200
    
    except Exception as e:
        return jsonify({
           'status':'Error',
             'message':str(e),
         }), 500
    finally:
        conn.close()
        
if __name__ == '__main__':
    app .run(port = 3000, debug = True)
    
