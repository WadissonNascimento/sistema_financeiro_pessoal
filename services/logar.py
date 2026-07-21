from utils.validadores import validar_email
from models.auth.cadastro import email_existe
from models.auth.login import buscar_senha_hash
from utils.seguranca import autenticar_senha

def autenticar_usuario(email, senha):
    if not validar_email(email):
        return {"mensagem":"email inválido"},400
    
    if not email_existe(email):
        return {"mensagem":"email ou senha incorretos."},400
    
    senha_hash = buscar_senha_hash(email)
    
    if autenticar_senha(senha, senha_hash):
        return {"mensagem":"login feito com sucesso."},200
    
    return {"mensagem":"email ou senha estão incorretos."},400