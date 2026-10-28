import sqlite3

conexao = sqlite3.connect("consultas_indices_graficos.db")

with open("ddl/criar_tabelas.sql", encoding="utf-8") as arquivo:
    conexao.executescript(arquivo.read())

conexao.close()