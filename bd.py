import pyodbc
import pymysql

#-----------------------------------------------------------------------------------------------------------------------
#CONEXION CON SQL SERVER

direccion_servidor = 'localhost'
nombre_bd = 'cinebd'
nombre_usuario = 'sa'
password = 'ITSVA2021'
try:
    conexion = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + 
                              direccion_servidor+';DATABASE='+nombre_bd+';UID='+nombre_usuario+';PWD=' + password)
    print("\n"*2)
    print("conexión exitosa con: SQL Server")
    
except Exception as e:
    print("Ocurrió un error al conectar a SQL Server: ", e) 

#----------------------------------------------------------------------------------------------------------------------
#CONEXION CON MYSQL

try:
	conexion = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='peliculas')
	print("Conexión exitosa con: MySQL")
except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
	print("Ocurrió un error al conectar: ", e)
