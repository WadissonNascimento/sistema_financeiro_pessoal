from utils.validadores import validar_email
from models.auth.cadastro import email_existe, inserir_usuario
from utils.segurança import converter_hash, gerar_uuid

def cadastrarUsuario(email, senha, nome):
    email = email.strip().lower()
    if not validar_email(email):
        return {"mensagem":"email inválido."}
    
    if email_existe(email):
        return  {"mensagem":"email já cadastrado."}
    
    senha_hash = converter_hash(senha)
    uuid = gerar_uuid()
    
    return inserir_usuario(uuid, nome, email, senha_hash)

