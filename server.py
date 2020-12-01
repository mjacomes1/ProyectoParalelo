from flask import Flask, render_template,request
import proccess as p
app = Flask(__name__)

con,cur = p.connectBD()

@app.route('/',methods=['GET'])
def hello_world():
    name = request.values.get('name')
    unix = request.values.get('unix')
    date = request.values.get('date')
    symbol = request.values.get('symbol')
    open = request.values.get('open')
    high = request.values.get('high')
    low = request.values.get('low')
    close = request.values.get('close')
    volume  = request.values.get('volume')

    p.createThread(name,unix,date,symbol,open,high,low,close,volume,cur,con)
    return "OK"
@app.route('/consulta',methods=['GET'])
def consulta():
    resp = p.consulta(cur,con)
    return "OK Consulto"+resp

@app.route('/eliminar',methods=['GET'])
def eliminar():
    resp = p.eliminar(cur,con)
    return "OK Elimino"+resp

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)  