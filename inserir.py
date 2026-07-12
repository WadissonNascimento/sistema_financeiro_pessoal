from database import conexao_banco

def inserir_contas_mensal(descricao, data_inicio, data_final, valor, status, vencimento):
    cursor, conexao = conexao_banco()
    
    try:
        cursor.execute('''
        INSERT INTO contas_mensais
        VALUES (%s, %s, %s, %s, %s, %s)
        ''',
        (descricao, data_inicio, data_final, valor, status, vencimento)
        )

        conexao.commit()

        return {'mensagem':'Item inserido com sucesso'}, 201
    
    except Exception as erro:
        conexao.rollback()

        return {"erro": str(erro)}, 500
    
    finally:
        cursor.close()
        conexao.close()

def inserir_gasto(descricao, valor):
    from datetime import datetime
    cursor, conexao = conexao_banco()

    try: 
        data = datetime.today().date()
        cursor.execute('''
        INSERT INTO gastos_mes
        VALUES(%s, %s, %s)
        ''',
        (descricao,valor,data)
        )

        conexao.commit()

        return {'mensagem':'Gasto registrado com sucesso'}, 201
    
    except Exception as erro:
        conexao.rollback()
        return {'erro':str(erro)},500
    
    finally:
        cursor.close()
        conexao.close()

def inserir_contas_fixa(descricao, valor, vencimento):
    cursor, conexao = conexao_banco()

    try: 
        cursor.execute('''
        INSERT INTO contas_fixas
        VALUES (%s, %s, %s)
        ''',
        (descricao, valor, vencimento)
        )

        conexao.commit()

        return {'mensagem':'Item inserido com sucesso'},201
    
    except Exception as erro:
        conexao.rollback()
        return {'erro':str(erro)},500

    finally:
        cursor.close()
        conexao.close()

