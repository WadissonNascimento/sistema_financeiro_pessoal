from werkzeug.security import generate_password_hash, check_password_hash
import uuid

def gerar_uuid():
    return uuid.uuid4()

def converter_hash(senha):
    return generate_password_hash(senha)

def autenticar_senha(senha, senha_hash):
     return check_password_hash(senha_hash, senha)