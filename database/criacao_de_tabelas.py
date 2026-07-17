from database.conexao import conexao_banco


def criar_tabelas():
    cursor, conexao = conexao_banco()

    try:
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS transacoes(
            id SERIAL PRIMARY KEY,
            descricao VARCHAR(100) NOT NULL,
            valor DECIMAL (10, 2) NOT NULL,
            tipo VARCHAR(20) CHECK (tipo IN ('RECEITA', 'DESPESA')) NOT NULL,
            categoria VARCHAR(50)NOT NULL,
            data DATE NOT NULL,
            status VARCHAR(20) CHECK (status in ('PAGO', 'PENDENTE')) DEFAULT 'PAGO'
        )
        ''')

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS recorrentes(
            id SERIAL PRIMARY KEY,
            descricao VARCHAR(100) NOT NULL,
            valor DECIMAL (10, 2) NOT NULL,
            quantidade_parcelas INTEGER NOT NULL,
            inicio DATE NOT NULL,
            final DATE NOT NULL,
            categoria VARCHAR(50) NOT NULL,
            dia_vencimento INTEGER CHECK (dia_vencimento BETWEEN 1 AND 31)
        )
        ''')

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios(
            id UUID PRIMARY KEY,
            nome VARCHAR(50) NOT NULL,
            email VARCHAR(50) NOT NULL UNIQUE,
            senha_hash VARCHAR(255) NOT NULL
        )
        ''')

        conexao.commit()
    finally:
        cursor.close()
        conexao.close()

criar_tabelas()