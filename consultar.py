from database import conexao_banco

def somar_total_de_contas():
    cursor, conexao = conexao_banco()
    cursor.execute('''
    SELECT SUM(valor)
    FROM contas_fixas
    ''')

    total = cursor.fetchone()

    return float(total[0] or 0)
    
def buscar_contas_fixas():
    cursor, conexao = conexao_banco()

    cursor.execute('''
    SELECT * FROM contas_fixas
    ''')

    consulta = cursor.fetchall()

    if consulta == []:
        conexao.rollback()
        return {"mensagem":"Nenhuma conta encontrada"}

    allContas = []

    for descricao, valor, dia_vencimento in consulta:
        allContas.append({
            "descricao": descricao,
            "valor":float(valor),
            "dia_vencimento": dia_vencimento
        })

    conexao.close()
    cursor.close()
    return allContas


def buscar_contas_mensais():
    cursor, conexao =  conexao_banco()

    cursor.execute('''
    SELECT * FROM contas_mensais
    ''')

    consulta = cursor.fetchall()

    if consulta == []:
        conexao.rollback()
        return {"mensagem":"Nenhuma conta encontrada"}
    
    allcontas = []
    
    for descricao, data_inicio, data_final, valor, status, vencimento in consulta:
        allcontas.append({
            "descricao": descricao,
            "data_inicio": data_inicio.isoformat(),
            "data_final":data_final.isoformat(),
            "valor":float(valor),
            "status": status,
            "vencimento":vencimento
        })

    conexao.close()
    cursor.close()
    return allcontas

def buscar_gastos():
    cursor, conexao = conexao_banco()

    cursor.execute('''
    SELECT * FROM gastos_mes
    ''')

    consulta = cursor.fetchall()

    if consulta == []:
        return {"mensagem":"Nenhum gasto encontrado"}
    
    allGastos = []

    for descricao, valor, data in consulta:
        allGastos.append({
            "descricao":descricao,
            "valor":float(valor),
            "data":data.isoformat()
        })


    conexao.close()
    cursor.close()
    return allGastos
