def validar_email(email):
    partes = email.split("@")

    if len(partes) != 2:
        return False
    
    usuario = partes[0]
    dominio = partes[1]

    if usuario == '' or dominio == '':
        return False
    
    if '.' not in dominio:
        return False
    
    caracteres_permitidos = 'abcdefghijklmnopqrstuvwxyz123456789.-_+'

    for caracteres in usuario:
        if caracteres not in caracteres_permitidos:
            return False
        
    for caracteres in dominio:
        if caracteres not in caracteres_permitidos:
            return False
    
    if usuario.startswith(".") or usuario.endswith("."):
        return False 
    
    if dominio.startswith(".") or dominio.endswith("."):
        return False 
    
    if ".." in usuario or ".." in dominio:
        return False
    
    dominio_partes = dominio.split(".")

    if len(dominio_partes) < 2:
        return False
    
    if len(dominio_partes[-1]) < 2:
        return False
    
    
    return True
    

