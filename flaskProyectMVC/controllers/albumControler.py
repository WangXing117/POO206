from flask import Blueprint , render_template, redirect, url_for, flash, request
from models.albumModel import *

albumsBP = Blueprint('albums',__name__)

@albumsBP.route('/')
def home(): #para que inicie la interfaz formulario por default
    try:
        consultaTodo = getAll()
        return render_template('formulario.html', errores = {}, albums = consultaTodo)
    except Exception as e:
        print('Error al consultar todo: '+str(e))
        return render_template('formulario.html', errores = {}, albums = [])
    
#################################################################
@albumsBP.route('/detalles/<albumID>')
def detalle(albumID): #para que inicie la interfaz formulario por default
    try:
        consultaTodo = getById(albumID)
        return render_template('consulta.html', errores = {}, album = consultaTodo)
    except Exception as e:
        print('Error al consultar el album: '+str(e))
        return render_template('consulta.html', errores = {}, album = [])

########################################3333
@albumsBP.route('/guardarAlbum',methods=['POST'])
def guardar():
    #lista de errores
    errores = {}
    #obtener los datos a insertar
    titulo = request.form.get('txtTitulo','').strip() #si hay espacios a la izq o der strip los quita
    artista = request.form.get('txtArtista','').strip() #si hay espacios a la izq o der strip los quita
    anio = request.form.get('txtAno','').strip() #si hay espacios a la izq o der strip los quita
    #manejo de campos vacios
    if not titulo:
        errores['txtTitulo'] = 'Nombre del album obligatorio'
    if not artista:
        errores['txtArtista'] = 'Nombre del artista obligatorio'
    if not anio:
        errores['txtAno'] = 'Año del album obligatorio'
    elif not anio.isdigit() or int(anio) < 1800 or int(anio) > 2030:
        errores['txtAno'] = 'En año solo ingresar un año valido'
        
    if not errores:
    #intentamos ejecutar el insert
        try:
            insertarAlbum(titulo, artista, anio)
            flash('Album guardado correctamente')
            return redirect(url_for('albums.home'))
        except Exception as e:
            flash('Album guardado correctamente')
            return redirect(url_for('albums.home'))
    return render_template('formulario.html', errores = errores)

####################################

@albumsBP.route('/editarAlbum/<alb>')
def verEditarAlbum(alb):
    errores = {}
    try:
        album = getById(alb)
        if album:
            return render_template('editarAlbum.html',album = album)
        else:
            errores["filaError"] = 'Error al obtener la fila de la base de datos'
    except Exception as e:
        print('Error durante el proceso de actualizacion: '+ str(e))
        errores['excepcion'] = 'Ha ocurrido un error durante la obtencion del album'
        
    return render_template('editarAlbum.html', errores = errores)

##############################################################33

@albumsBP.route('/editarAlbum', methods=['POST'])
def editarAlbum():
    errores = {}
    try:
        titulo = request.form.get('txtTitulo','').strip() #si hay espacios a la izq o der strip los quita
        artista = request.form.get('txtArtista','').strip() #si hay espacios a la izq o der strip los quita
        anio = request.form.get('txtAno','').strip() #si hay espacios a la izq o der strip los quita
        IDAlbum = request.form.get('idAlbum','')
        print()
        #manejo de campos vacios
        if not titulo:
            errores['txtTitulo'] = 'Nombre del album obligatorio'
        if not artista:
            errores['txtArtista'] = 'Nombre del artista obligatorio'
        if not anio:
            errores['txtAno'] = 'Año del album obligatorio'
        elif not anio.isdigit() or int(anio) < 1800 or int(anio) > 2030:
            errores['txtAno'] = 'En año solo ingresar un año valido'
            
        if not errores:
            updateAlbum(titulo,artista,anio,IDAlbum)
            flash('Album actualizado correctamente')
            return redirect(url_for('albums.home'))
    except Exception as e:
        print('Error al intentar actualizar en la base de datos: '+ str(e))
        errores['updateTable'] = 'Error al actualizar en la base de datos'
    return render_template('editarAlbum.html', errores = errores, album = [])

###################################################################################3

@albumsBP.route('/eliminarAlbum/<idAlbum>', methods=['GET', 'POST'])
def eliminarAlbum(idAlbum):
    errores = {}
    nombreAlbum = []

    try:
   
        if request.method == 'POST':
            idA = request.form.get('idAlbum', '').strip()
            if not idA:
                errores['idError'] = 'ID no retornado'
            else:
                deleteAlbum(idAlbum)
                flash('Álbum eliminado correctamente')
                return redirect(url_for('albums.home'))

        elif request.method == 'GET':
            nom = getDeleteAlbum(idAlbum)
            if not nom:
                errores['nombreError'] = 'No se encontró el álbum o ya fue eliminado'
            else:
                nombreAlbum = nom

    except Exception as e:
        print('Error en eliminarAlbum: ' + str(e))
        errores['eliminarError'] = 'Error en la operación'

    return render_template('eliminarAlbum.html', errores=errores, nombreAlbum=nombreAlbum)