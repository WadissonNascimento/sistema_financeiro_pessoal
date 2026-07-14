from database.conexao import conexao_banco

def buscar_transacoes():
    try:
        cursor, conexao = conexao_banco()

        cursor.execute('''
        SELECT descricao, valor, tipo, categoria, data, status, id
        FROM transacoes
        ''')

        transacoes = cursor.fetchall()

        todas_transacoes = []

        if transacoes == []:
            return []
        
        for descricao, valor, tipo, categoria, data, status in transacoes:
            todas_transacoes.append({
                "descricao":descricao,
                "valor":float(valor),
                "tipo":tipo,
                "categoria":categoria,
                "data":data.isoformat(),
                "status":status
            })

        return todas_transacoes
    
    finally:
        cursor.close()
        conexao.close()