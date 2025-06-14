import pyodbc

# Establecer la conexión

def obtenerConexion():
    try:
        conn = pyodbc.connect('DRIVER={SQL Server};SERVER=WANGXING;DATABASE=Flaskpoo;Trusted_Connection=yes;') 
        print('!!!!!!!!!!!!! conexion exitosa !!!!!!!!!!!!!!!!!!!!!!!!!!1')
        return conn
    
    except Exception as e:
        return 0
