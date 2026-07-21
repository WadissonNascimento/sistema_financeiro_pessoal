from utils.validadores import validar_email
from models.auth.cadastro import email_existe, inserir_usuario
from utils.seguranca import converter_hash, gerar_uuid

def cadastrarUsuario(nome, email, senha):
    
    email = email.strip().lower()

    if not validar_email(email):
        return {
            "mensagem":"email inválido.",
            "sucesso":False
        }

    if email_existe(email):
        return  {
            "mensagem":"email já cadastrado.",
            "sucesso":False
        }
    
    senha_hash = converter_hash(senha)
    uuid = gerar_uuid()
    
    if inserir_usuario(uuid, nome, email, senha_hash):
        return {
            "sucesso":True,
            "mensagem":"usuário cadastrado com sucesso."
        }
    
    return {
        "sucesso":False,
        "mensagem":"Erro ao cadastrar o usuário."
    }

