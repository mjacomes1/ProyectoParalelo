from config import config as c

import psycopg2

def conectar():
    conexion = None
    try:
        params = c.config() 
        conexion = psycopg2.connect(**params)
    except Exception as error:
        print(error)
    return conexion