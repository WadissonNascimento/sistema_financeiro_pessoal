from flask import Flask, render_template, jsonify
from database.criacao_de_tabelas import criar_tabelas
from models.transacoes import buscar_transacoes
from models.recorrencias import buscar_recorrencias

criar_tabelas()

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.get('/')
def buscar():
    return jsonify({
        "transacoes":buscar_transacoes(),
        "recorrencias":buscar_recorrencias()
    })


if __name__ == '__main__':
    app.run(debug=True)
