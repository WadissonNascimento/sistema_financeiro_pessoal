from database.conexao import conexao_banco

def buscar_recorrencias():
    try:
        cursor, conexao = conexao_banco()

        cursor.execute('''
        SELECT descricao, valor, quantidade_parcelas, inicio, final, categoria, dia_vencimento, id
        FROM recorrentes
        ''')

        recorrentes = cursor.fetchall()

        if recorrentes == []:
            return []
        
        todas_recorrencias = []
        
        for descricao, valor, quantidade_parcelas, inicio, final, categoria, dia_vencimento in recorrentes:
            todas_recorrencias.append({
                "descricao":descricao,
                "valor":float(valor),
                "quantidade_parcelas":quantidade_parcelas,
                "inicio":inicio.isoformat(),
                "final":final.isformat(),
                "categoria":categoria,
                "dia_vencimento":dia_vencimento
            })

        return todas_recorrencias
    finally:
        cursor.close()
        conexao.close()