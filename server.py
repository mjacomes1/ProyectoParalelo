from flask import Flask, render_template,request
import proccess as p
app = Flask(__name__)

#cur = p.connectBD()

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

    p.insert(name,unix,date,symbol,open,high,low,close,volume,cur)

    return "Hola mundo"

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)  