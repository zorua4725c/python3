from flask import Flask
import random

lista = ['Afectación del sueño, como problemas para dormir o insomnio','Dificultades para sostener la atención y concentrarse','Dificultades a nivel de la memoria','Ansiedad e hiperestimulación']
moneda = ['Cara','Cruz']

app = Flask(__name__)

@app.route("/")
def hello_world():
    return f'<p>Hola</p><a href="/random_fact">¡Ver un dato aleatorio!</a><a href="/moneda">¡lanza una moneda!</a>'

@app.route("/random_fact")
def azar():
    return f'<p>{random.choice(lista)}</p>'

@app.route("/moneda")
def money():
    return f'<p>{random.choice(moneda)}</p>'

app.run(debug=True)