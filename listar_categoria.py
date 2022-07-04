import sqlite3
conexao = sqlite3.connect('m2s4dados.sqlite3')
sql = "SELECT id, nome, titulos, confederacao FROM selecao; "
cursor.execute()
conexao.commit()
conexao.close()