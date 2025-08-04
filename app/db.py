# db.py
import mysql.connector
import os

def conectar():
    try:
        conn = mysql.connector.connect(
            host=os.getenv("DB_HOST", "localhost"),
            user=os.getenv("DB_USER", "root"),
            password=os.getenv("DB_PASSWORD", "password"),
            database=os.getenv("BD_NAME", "comissoes"),
        )
        return conn
    except mysql.connector.Error as err:
        print(f"Erro ao conectar ao banco de dados: {err}")
        raise

def get_dashbord_summary():
    conn = None
    cursor = None
    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT SUM(valor) AS total_cargas, SUM(valor * percentual / 100) AS total_comissoes FROM cargas")
        result = cursor.fetchone()

        total_cargas = result[0] if result[0] is not None else 0.00
        total_comissoes = result[1] if result[1] is not None else 0.00

        from decimal import Decimal
        return {
            "total_cargas": float (total_cargas),
            "total_comissoes": float (total_comissoes)
        }
    except Exception as e:
        print(f"Erro ao obter resumo do dashboard: {e}")
        return None
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
            