from config import bd as base
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
import numpy as np
import mysql.connector
import threading

info = np.empty(shape=[0])

threadLock = threading.Lock() 

#conectar en la BD
def connectBD():
    conn = base.conectar()
    cur = conn.cursor()
    return conn,cur

#Crear hilos
def createThread(name,unix,date,symbol,open,high,low,close,volume,cur,con):
    p = threading.Thread(target=insert, args=(name,unix,date,symbol,open,high,low,close,volume,cur,con))
    p.start()
    p.join()


#Insertar en Lista
def insert(name,unix,date,symbol,open,high,low,close,volume,cur,con):
    threadLock.acquire()
    #if con == None: 
    #    con,cur = connectBD()
    global info
    result = np.where(info == unix)

    if len(result[0]) == 0:
        try:
            cur.execute('insert into "proyecto" values(%s,%s,%s,%s,%s,%s,%s,%s,%s)',(unix,date,symbol,open,high,low,close,volume,name))
            con.commit()
            info = np.append(info,[unix])
        except Exception as identifier:
            cur.execute("ROLLBACK")
            con.commit()
            info = np.append(info,[unix])
            print("Error",identifier)
    threadLock.release()

#Eliminar toda la bd
def eliminar(cur,con):
    try:
        cur.execute('delete from proyecto')
        con.commit()
        row = cur.rowcount
        print("Se elimino ",row)
        return row
    except Exception as identifier:
        print("Errror" , identifier)

def consulta(cur,con):
    try:
        cur.execute("Select * from proyecto")
        rows = cur.fetchall()
        cont = 0
        # Do stuff with the data
        for row in rows:
            cont+=1
            print("___  = ___ ")

            print ("Unix = {} ".format(row[0]))
            print ("Date = {}".format(row[1]))
            print("Symbol = {}".format(row[2]))
            print("Open = {}".format(row[3]))
            print("High = {}".format(row[4]))
            print("Low = {}".format(row[5]))
            print("Close = {}".format(row[6]))
            print("Volume = {}".format(row[7]))
            print("Name = {}".format(row[8]))
        print("Total",cont)
        return cont
    except Exception as identifier:
        print("Error",identifier)

