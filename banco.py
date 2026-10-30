import sqlite3
from marcas import MARCAS

NOME_BANCO = "phishing.db"

def criar_banco():
    conexao = sqlite3.connect(NOME_BANCO)
    cursor = conexao.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS marcas (
            marca TEXT PRIMARY KEY,
            dominio_oficial TEXT NOT NULL
        )
    """)

    for marca, oficial in MARCAS.items():
        cursor.execute(
            "INSERT OR IGNORE INTO marcas(marca, dominio_oficial) VALUES (?, ?)",
            (marca, oficial),
        )

    conexao.commit()
    conexao.close()

def carregar_marcas():
    conexao = sqlite3.connect(NOME_BANCO)
    cursor = conexao.cursor()

    cursor.execute("SELECT marca, dominio_oficial FROM marcas")
    linhas = cursor.fetchall()

    conexao.close
    return dict(linhas)
