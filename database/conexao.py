import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

def conexao_banco():
    conexao = psycopg2.connect(
        host='localhost',
        database='sistema_financeiro_pessoal',
        user='postgres',
        password=os.getenv('key_db'),
        port='5432'
    )

    cursor = conexao.cursor()
    return cursor, conexao
