from config import config as c
import mysql.connector

def conectar():
    conexion = None
    try:
        params = c.config() 
        conexion = mysql.connector.connect(**params)
    except Exception as error:
        print(error)
    return conexion