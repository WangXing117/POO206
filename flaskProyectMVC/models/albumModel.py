from conexion_sqlserver import obtenerConexion

#metodo para obtener albunes activos
def getAll():
    conn = obtenerConexion()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Album WHERE Estado = 1')
    consultaTodo = cursor.fetchall()
    cursor.close()
    
    return consultaTodo

#metodo para obtener album por ID
def getById(id):
    conn = obtenerConexion()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Album WHERE ID = (?)',id)
    consultaTodo = cursor.fetchone()
    cursor.close()
    
    return consultaTodo

#metodo para insertar album
def insertarAlbum(titulo,artista,anio):
    conn = obtenerConexion()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO Album(Titulo,Artista,Ano_Publicacion) VALUES (?,?,?)',(titulo,artista,anio))
    conn.commit()
    cursor.close()
    
#metodo para editar album
def updateAlbum(titulo,artista,anio,id):
    conn = obtenerConexion()
    cursor = conn.cursor()
    cursor.execute('UPDATE Album SET Titulo = ?, Artista = ?, Ano_Publicacion = ? WHERE ID = (?)',(titulo,artista,anio,id))
    conn.commit()
    cursor.close()
    
#metodo para eliminar album
def deleteAlbum(id):
    conn = obtenerConexion()
    cursor = conn.cursor()
    cursor.execute('UPDATE Album SET Estado = ? WHERE ID = ?', (0, id))
    conn.commit()
    cursor.close()
    
#metodo para obtener ifnormacion del album eliminar
def getDeleteAlbum(id):
        conn = obtenerConexion()
        cursor = conn.cursor()
        cursor.execute('SELECT ID, Titulo, Artista FROM Album WHERE ID = ? AND Estado = 1', (id,))
        nom = cursor.fetchone()
        
        return nom
