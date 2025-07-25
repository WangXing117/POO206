#Importaciones importante
from flask import Flask, jsonify, render_template
from conexion_sqlserver import obtenerConexion
from controllers.albumControler import albumsBP

app = Flask(__name__)
app.secret_key = 'mysecretkey'

app.register_blueprint(albumsBP)

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

# @app.route('/')
# def home(): #para que inicie la interfaz formulario por default
#     try:
#         # conn = obtenerConexion()
#         # cursor = conn.cursor()
#         # cursor.execute('SELECT * FROM Album WHERE Estado = 1')
#         # consultaTodo = cursor.fetchall()
#         return render_template('formulario.html', errores = {}, albums = consultaTodo)
#     except Exception as e:
#         print('Error al consultar todo: '+str(e))
#         return render_template('formulario.html', errores = {}, albums = [])
#     finally:
#         if cursor:
#             cursor.close()
            
# @app.route('/detalles/<albumID>')
# def detalle(albumID): #para que inicie la interfaz formulario por default
#     try:
#         # conn = obtenerConexion()
#         # cursor = conn.cursor()
#         # cursor.execute('SELECT * FROM Album WHERE ID = (?)',albumID)
#         # consultaTodo = cursor.fetchone()
#         return render_template('consulta.html', errores = {}, album = consultaTodo)
#     except Exception as e:
#         print('Error al consultar el album: '+str(e))
#         return render_template('consulta.html', errores = {}, album = [])
#     finally:
#         if cursor:
#             cursor.close()

# @app.route('/guardarAlbum',methods=['POST'])
# def guardar():
#     #lista de errores
#     errores = {}
#     #obtener los datos a insertar
#     titulo = request.form.get('txtTitulo','').strip() #si hay espacios a la izq o der strip los quita
#     artista = request.form.get('txtArtista','').strip() #si hay espacios a la izq o der strip los quita
#     anio = request.form.get('txtAno','').strip() #si hay espacios a la izq o der strip los quita
#     #manejo de campos vacios
#     if not titulo:
#         errores['txtTitulo'] = 'Nombre del album obligatorio'
#     if not artista:
#         errores['txtArtista'] = 'Nombre del artista obligatorio'
#     if not anio:
#         errores['txtAno'] = 'Año del album obligatorio'
#     elif not anio.isdigit() or int(anio) < 1800 or int(anio) > 2030:
#         errores['txtAno'] = 'En año solo ingresar un año valido'
        
#     if not errores:
#     #intentamos ejecutar el insert
#         try:
#             conn = obtenerConexion()
#             cursor = conn.cursor()
#             # cursor.execute('INSERT INTO Album(Titulo,Artista,Ano_Publicacion) VALUES (?,?,?)',(titulo,artista,anio))
#             # conn.commit() #confirmacion del cambio
#             flash('Album guardado correctamente')
#             return redirect(url_for('home'))
#         except Exception as e:
#             conn.rollback() #revierte cualquier cambio
#             flash('Album guardado correctamente')
#             return redirect(url_for('home'))
#         finally:
#             conn.close() #cierra la conexion
#     return render_template('formulario.html', errores = errores)
        
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

# @app.route('/editarAlbum/<alb>')
# def verEditarAlbum(alb):
#     errores = {}
#     try:
#         conn = obtenerConexion()
#         cursor = conn.cursor()
#         cursor.execute('SELECT * FROM Album WHERE ID = (?)',(alb))
#         album = cursor.fetchone()
#         if album:
#             return render_template('editarAlbum.html',album = album)
#         else:
#             errores["filaError"] = 'Error al obtener la fila de la base de datos'
#     except Exception as e:
#         print('Error durante el proceso de actualizacion: '+ str(e))
#         errores['excepcion'] = 'Ha ocurrido un error durante la obtencion del album'
        
#     finally:
#         if cursor:
#             cursor.close()
#         if conn:
#             conn.close()
#     return render_template('editarAlbum.html', errores = errores)

# @app.route('/editarAlbum', methods=['POST'])
# def editarAlbum():
#     errores = {}
#     try:
#         titulo = request.form.get('txtTitulo','').strip() #si hay espacios a la izq o der strip los quita
#         artista = request.form.get('txtArtista','').strip() #si hay espacios a la izq o der strip los quita
#         anio = request.form.get('txtAno','').strip() #si hay espacios a la izq o der strip los quita
#         IDAlbum = request.form.get('idAlbum','')
#         print()
#         #manejo de campos vacios
#         if not titulo:
#             errores['txtTitulo'] = 'Nombre del album obligatorio'
#         if not artista:
#             errores['txtArtista'] = 'Nombre del artista obligatorio'
#         if not anio:
#             errores['txtAno'] = 'Año del album obligatorio'
#         elif not anio.isdigit() or int(anio) < 1800 or int(anio) > 2030:
#             errores['txtAno'] = 'En año solo ingresar un año valido'
            
#         if not errores:
#             conn = obtenerConexion()
#             cursor = conn.cursor()
#             cursor.execute('UPDATE Album SET Titulo = ?, Artista = ?, Ano_Publicacion = ? WHERE ID = (?)',(titulo,artista,anio,IDAlbum))
#             conn.commit() #confirmacion del cambio
#             flash('Album actualizado correctamente')
#             return redirect(url_for('home'))
#     except Exception as e:
#         print('Error al intentar actualizar en la base de datos: '+ str(e))
#         errores['updateTable'] = 'Error al actualizar en la base de datos'
#     return render_template('editarAlbum.html', errores = errores, album = [])

# @app.route('/eliminarAlbum/<idAlbum>', methods=['GET', 'POST'])
# def eliminarAlbum(idAlbum):
#     errores = {}
#     nombreAlbum = []

#     try:
#         conn = obtenerConexion()
#         cursor = conn.cursor()

#         if request.method == 'POST':
#             idA = request.form.get('idAlbum', '').strip()
#             if not idA:
#                 errores['idError'] = 'ID no retornado'
#             else:
#                 cursor.execute('UPDATE Album SET Estado = ? WHERE ID = ?', (0, idA))
#                 conn.commit()
#                 flash('Álbum eliminado correctamente')
#                 return redirect(url_for('home'))

#         elif request.method == 'GET':
#             cursor.execute('SELECT ID, Titulo, Artista FROM Album WHERE ID = ? AND Estado = 1', (idAlbum,))
#             nom = cursor.fetchone()
#             if not nom:
#                 errores['nombreError'] = 'No se encontró el álbum o ya fue eliminado'
#             else:
#                 nombreAlbum = nom

#     except Exception as e:
#         print('Error en eliminarAlbum: ' + str(e))
#         errores['eliminarError'] = 'Error en la operación'

#     finally:
#         if 'cursor' in locals():
#             cursor.close()
#         if 'conn' in locals():
#             conn.close()

#     return render_template('eliminarAlbum.html', errores=errores, nombreAlbum=nombreAlbum)

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
    
