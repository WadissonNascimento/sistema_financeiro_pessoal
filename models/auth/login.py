from database.conexao import conexao_banco

def buscar_senha_hash(email):
    cursor, conexao = conexao_banco()

    try: 
        cursor.execute('''
        SELECT senha_hash FROM usuarios
        WHERE email = %s
        ''',
        (email,)
        )

        senha_hash = cursor.fetchone()

        return senha_hash[0]

    except Exception as erro:
        conexao.rollback()
        print(erro)

    finally:
        cursor.close()
        conexao.close()   