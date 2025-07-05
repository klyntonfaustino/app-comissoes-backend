import mysql.connector
from mysql.connector import Error

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

