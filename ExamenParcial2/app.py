from flask import Flask, jsonify, render_template, request, flash, url_for, redirect
from conexion import obtenerConexion
from flask_mysqldb import MySQL
import MySQLdb
import pyodbc

app = Flask(__name__)
app.secret_key = 'mysecretkey'

@app.route('/')
def home():
    errores = {}
    print('Ingresando a formulario y lista de comentarios')
    try:
        conn = obtenerConexion()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Restaurantes WHERE Estatus = 1')
        consultaTodo = cursor.fetchall()
        print(f'aquello obtenido del select de restaurantes {consultaTodo}')
        if not consultaTodo:
            errores['consultaError'] = "Error al obtener lista de comentarios"
        if errores:
            print(f'existen los errores: {errores}')
        else:
            return render_template('restaurantes.html', errores = {}, albums = consultaTodo)
    except Exception as e:
        print(f'Ha sucesido un error al jalar la lista de comentarios: {str(e)}')
        errores['dbError'] = 'Excepcion durante la obtencion de la lista'
    finally:
        if cursor:
            cursor.close()
        
    render_template('restaurantes.html', errores = errores, albums = [])
    
@app.route('/guardarComentario',methods=['POST'])
def guardar():
    print('Intentando guardar comentario')
    #lista de errores
    errores = {}
    #obtener los datos a insertar
    titulo = request.form.get('txtTitulo','').strip() #si hay espacios a la izq o der strip los quita
    artista = request.form.get('txtArtista','').strip() #si hay espacios a la izq o der strip los quita
    comentario = request.form.get('txtComentario','').strip()
    anio = request.form.get('txtAno','').strip() #si hay espacios a la izq o der strip los quita
    print(f'Cambios llegados desde el formulario {titulo}, {artista}, {comentario}, {anio} and {type(anio)}')
    #manejo de campos vacios
    if not titulo:
        errores['txtTitulo'] = 'Nombre del restaurante obligatorio'
    if not artista:
        errores['txtArtista'] = 'Tipo de comida obligatorio'
    if not comentario:
        errores['txtComentario'] = 'Comentario obligatorio'
    if not anio:
        errores['txtAno'] = 'Calificacion obligatoria'
    elif not anio.isdigit() or int(anio) < 0 or int(anio) > 5:
        errores['txtAno'] = 'La calificacion es de 1 a 5'
    
    if not errores:
    #intentamos ejecutar el insert
        try:
            print('Comenzando a agregar')
            conn = obtenerConexion()
            cursor = conn.cursor()
            cursor.execute('INSERT INTO Restaurantes(Titulo,TipoComida,Comentario,Calificacion,Estatus) VALUES (?,?,?,?,?)',(titulo,artista,comentario,anio,1))
            conn.commit() #confirmacion del cambio
            flash('Comentario guardado correctamente')
            return redirect(url_for('home'))
        except Exception as e:
            conn.rollback() #revierte cualquier cambio
            flash('Comentario guardado correctamente')
            return redirect(url_for('home'))
        finally:
            if conn:
                conn.close() #cierra la conexion
    return render_template('restaurantes.html', errores = errores)

@app.route('/detalles/<albumID>')
def detalle(albumID): #para que inicie la interfaz formulario por default
    errores = {}
    print('Intentando consultar el comentario')
    try:
        conn = obtenerConexion()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Restaurantes WHERE ID = (?)',albumID)
        consultaTodo = cursor.fetchone()
        print(f'Comentario obtendio: {consultaTodo}')
        return render_template('consulta.html', errores = {}, album = consultaTodo)
    except Exception as e:
        errores['dbError'] = 'Error al obtener el comentario'
        print('Error al consultar el comentario: '+str(e))
        return render_template('consulta.html', errores = errores, album = [])
    finally:
        if cursor:
            cursor.close()
            
@app.route('/editarAlbum/<alb>')
def verEditarAlbum(alb):
    errores = {}
    try:
        conn = obtenerConexion()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Restaurantes WHERE ID = (?)',(alb))
        album = cursor.fetchone()
        if album:
            return render_template('editarAlbum.html',album = album)
        else:
            errores["filaError"] = 'Error al obtener la fila de la base de datos'
    except Exception as e:
        print('Error durante el proceso de actualizacion: '+ str(e))
        errores['excepcion'] = 'Ha ocurrido un error durante la obtencion del album'
        
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
    return render_template('editarAlbum.html', errores = errores, album = None)

@app.route('/editarAlbum', methods=['POST'])
def editarAlbum():
    errores = {}
    try:
        titulo = request.form.get('txtTitulo','').strip() #si hay espacios a la izq o der strip los quita
        artista = request.form.get('txtArtista','').strip() #si hay espacios a la izq o der strip los quita
        anio = request.form.get('txtAno','').strip() #si hay espacios a la izq o der strip los quita
        IDAlbum = request.form.get('idAlbum','')
        comentario = request.form.get('txtComentario','').strip()
        print()
        #manejo de campos vacios
        if not titulo:
            errores['txtTitulo'] = 'Nombre del restaurante obligatorio'
        if not artista:
            errores['txtArtista'] = 'Tipo de comida obligatoria'
        if not anio:
            errores['txtAno'] = 'Comentario obligatorio'
        elif not anio.isdigit() or int(anio) < 0 or int(anio) > 5:
            errores['txtAno'] = 'En año solo ingresar un año valido'
        if not comentario:
            errores['txtComentario'] = 'Comentario obligatorio'
            
        if not errores:
            conn = obtenerConexion()
            cursor = conn.cursor()
            cursor.execute('UPDATE Restaurantes SET Titulo = ?, TipoComida = ?, Comentario = ?, Calificacion = ? WHERE ID = (?)',(titulo,artista,comentario,anio,IDAlbum))
            conn.commit() #confirmacion del cambio
            flash('Comentario actualizado correctamente')
            return redirect(url_for('home'))
    except Exception as e:
        print('Error al intentar actualizar en la base de datos: '+ str(e))
        errores['updateTable'] = 'Error al actualizar en la base de datos'
    return render_template('editarAlbum.html', errores = errores, album = [])

@app.route('/eliminarAlbumA', methods=['POST'])
def eliminarAlbumA():
    print('Comenzando a eliminar')
    errores = {}

    try:
        conn = obtenerConexion()
        cursor = conn.cursor()
        idA = request.form.get('idAlbum', '').strip()
        if not idA:
                errores['idError'] = 'ID no retornado'
        else:
                cursor.execute('UPDATE Restaurantes SET Estatus = ? WHERE ID = ?', (0, idA))
                conn.commit()
                flash('Álbum eliminado correctamente')
                return redirect(url_for('home'))
    except Exception as e:
        print('Error en eliminarAlbum: ' + str(e))
        errores['eliminarError'] = 'Error en la operación'

    finally:
        if 'cursor':
            cursor.close()
        if 'conn':
            conn.close()
    return render_template('eliminarAlbum.html', errores=errores, nombreAlbum=None)

@app.route('/eliminarAlbum/<idAlbum>',methods=['GET'])
def eliminarAlbum(idAlbum):
    print('Entrando a eliminar comentario')
    errores = {}
    nombreAlbum = []
    try:
        conn = obtenerConexion()
        cursor = conn.cursor()


        cursor.execute('SELECT ID, Titulo, Calificacion FROM Restaurantes WHERE ID = ? AND Estatus = 1', (idAlbum,))
        nom = cursor.fetchone()
        print(f'Esto llego a eliminar {nom}')
        if not nom:
            errores['nombreError'] = 'No se encontró el comentario o ya fue eliminado'
        else:
            nombreAlbum = nom
            return render_template('eliminarAlbum.html', errores=errores, nombreAlbum=nombreAlbum)
    except Exception as e:
        print('Error en eliminarAlbum: ' + str(e))
        errores['eliminarError'] = 'Error en la operación'

    finally:
        if 'cursor':
            cursor.close()
        if 'conn':
            conn.close()

    return render_template('eliminarAlbum.html', errores=errores, nombreAlbum=None)


if __name__ == '__main__':
    app .run(port = 3000, debug = True)

