from werkzeug.security import generate_password_hash
import uuid

def gerar_uuid():
    return uuid.uuid4()

def converter_hash(senha):
    return generate_password_hash(senha)