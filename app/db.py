# db.py
import mysql.connector
from mysql.connector import Error
from decimal import Decimal

def conectar():
    try:
        conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="maju9988",
            database="comissao_db",
            port=3306
        )

        if conexao.is_connected():
            print("Conectado ao MySQL com sucesso!")
            return conexao
    except Error as e:
        print(f"Erro ao conectar ao MySQL: {e}")
        return None

def get_dashbord_summary():
    conn = None
    cursor = None
    try:
        conn = conectar()
        if conn is None:
            print("Não foi possível conectar ao banco de dados.")
            return None
        cursor = conn.cursor()


        cursor.execute("SELECT SUM(valor) FROM cargas")
        total_cargas_bruto = cursor.fetchone()[0]
        total_cargas = Decimal(str(total_cargas_bruto)) if total_cargas_bruto is not None else Decimal('0.00')

        cursor.execute("SELECT SUM(valor * percentual / 100) FROM cargas")
        total_comissoes_bruto = cursor.fetchone()[0]
        total_comissoes = Decimal(str(total_comissoes_bruto)) if total_comissoes_bruto is not None else Decimal('0.00')

        return{
            "total_cargas": total_cargas,
            "total_comissoes": total_comissoes
        }
    except Error as err:
        print(f"Erro ao obter resumo do dashboard: {err}")
        return None
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
            