from database import conexao_banco

def excluir_conta_mensal(descricao):
    cursor, conexao = conexao_banco()

    try: 
        cursor.execute('''
        DELETE FROM contas_mensais
        WHERE descricao = %s
        ''',
        (descricao,)
        )
        
        conexao.commit()
        return {'mensagem':'Item excluído com sucesso'}, 200
    
    except Exception as erro:
        conexao.rollback()
        return {'erro':str(erro)}, 404
    
    finally:
        cursor.close()
        conexao.close()

def excluir_conta_fixa(descricao):
    cursor, conexao = conexao_banco()

    try:
        cursor.execute('''
        DELETE FROM contas_fixas
        WHERE descricao = %s
        ''',
        (descricao,)
        )

        conexao.commit()
        return {'mensagem':'Item excluído com sucesso'}, 200

    except Exception as erro:
        conexao.rollback()
        return {'erro':str(erro)}, 404
    
    finally:
        cursor.close()
        conexao.close()

def excluir_gasto(descricao):
    cursor, conexao = conexao_banco()

    try:
        cursor.execute('''
        DELETE FROM gastos_mes
        WHERE descricao = %s
        ''',
        (descricao,)
        )

        conexao.commit()
        return {'mensagem':'Item excluído com sucesso'}, 200

    except Exception as erro:
        conexao.rollback()
        return {'erro':str(erro)}, 404
    
    finally:
        cursor.close()
        conexao.close()