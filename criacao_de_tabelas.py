from database import conexao_banco


def criar_tabelas():
    cursor, conexao = conexao_banco()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS gastos_mes(
        descricao VARCHAR(20) NOT NULL,
        valor DECIMAL(10,2) NOT NULL,
        data DATE NOT NULL
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS contas_mensais(
        descricao VARCHAR(20) NOT NULL,
        data_inicio DATE NOT NULL,
        data_final DATE NOT NULL,
        valor DECIMAL(10,2) NOT NULL,
        status VARCHAR(20) CHECK (status IN ('PAGO', 'PENDENTE', 'EM ATRASO')) NOT NULL,
        vencimento INTEGER NOT NULL
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS contas_fixas(
        descricao VARCHAR(20) NOT NULL,
        valor DECIMAL(10,2) NOT NULL,
        vencimento DATE NOT NULL
    );
    """)

    conexao.commit()

    cursor.close()
    conexao.close()