from database.conexao import conexao_banco

def email_existe(email):
    cursor, conexao = conexao_banco()
    try:
        cursor.execute('''
        SELECT email FROM usuarios
        WHERE email = %s
        ''',
        (email,)
        )

        consulta = cursor.fetchone()

        if consulta:
            return True
        
        return False


    finally:
        cursor.close()
        conexao.close()

def inserir_usuario(uuid, nome, email, senha_hash):
    cursor, conexao = conexao_banco()

    try:
        cursor.execute('''
        INSERT INTO usuarios (id, nome, email, senha_hash)
        VALUES(%s, %s, %s, %s)
        ''',
        (str(uuid), nome, email, senha_hash))

        conexao.commit()

        return {"mensagem":"sucesso usuário cadastrado com sucesso."}

    except Exception as e:
        conexao.rollback()
        return {"erro":str(e)}
    
    finally:
        cursor.close()
        conexao.close()