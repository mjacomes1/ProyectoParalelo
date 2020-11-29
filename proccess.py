from config import bd as base

import mysql.connector
info = []


def connectBD():
    conn = base.conectar()
    return cur = conn.cursor()

#Insertar en Lista
def insert(name,unix,date,symbol,open,high,low,close,volume,cur):
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

def escribir(line):
    f = open('test.txt','a')
    f.write(line)
    f.close()