from flask import  Flask, request, jsonify
from database.criacao_de_tabelas import criar_tabelas
from models.transacoes import buscar_transacoes
from models.recorrencias import buscar_recorrencias
from services.cadastrar import cadastrarUsuario
from services.logar import autenticar_usuario

criar_tabelas()

app = Flask(__name__)

@app.route('/')
def home():
    return "testes"

@app.post('/cadastrar')
def cadastrar_Usuario():
    dados = request.get_json()

    nome = dados.get("nome")
    email = dados.get("email")
    senha = dados.get("senha")

    if not nome or not nome.strip():
        return jsonify({
            "mensagem":"o nome é obrigatório."
        }),400
    
    if not email or not email.strip():
        return jsonify({
            "mensagem":"o email é obrigatório."
        }),400
    
    if not senha or not senha.strip():
        return jsonify({
            "mensagem":"a senha é obrigatório."
        }),400

    
    resultado = cadastrarUsuario(nome, email, senha)

    if not resultado["sucesso"]:
        return jsonify(resultado),400
    
    return jsonify(resultado),201

@app.post('/login')
def login():
    dados = request.get_json()

    email = dados.get('email')
    senha = dados.get('senha')

    if not email or not email.strip() or not senha or not senha.strip():
        return jsonify({
            "mensagem": "preencha os dados corretamente"
        }), 400

    email = email.strip()
    senha = senha.strip()
    
    return autenticar_usuario(email, senha)
    
    

if __name__ == '__main__':
    app.run(debug=True)