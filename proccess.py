#from config import bd as base

#import mysql.connector
info = []

#onectar en la BD
def connectBD():
    conn = base.conectar()
    cur = conn.cursor()
    return cur

#Insertar en Lista
#def insert(name,unix,date,symbol,open,high,low,close,volume,cur):
def insert(name,unix,date,symbol,open,high,low,close,volume):
    try: 
        if len(info) > 0:
            temp = []
            for i in info:
                temp.append(i[1])
            temp.index(unix)
        else:
            info.index(unix)     
    except Exception as identifier:
        info.append([name,unix,date,symbol,open,high,low,close,volume])
        #Linea para insertar en la BD
        #cur.execute()
        escribir(name+"\t"+unix+"\t"+date+"\t"+symbol+"\t"+open+"\t"+high+"\t"+low+"\t"+close+"\t"+volume+"\n")
        print("Inserto", identifier,"\n",len(info))
#Escribir en Txt
def escribir(line):
    f = open('test.txt','a')
    f.write(line)
    f.close()

#Leer en Txt
def leer():
    with open('test.txt', 'r') as f:
        contenido = f.read()
        print(contenido)
    
        return contenido

#Borrar en Txt
def borrar():
    with open('test.txt', 'w') as f:
        f.write("")
