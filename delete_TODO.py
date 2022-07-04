import sqlite3
conexao = sqlite3.connect('m2s4dados.sqlite3')

id = input('Qual você ID deseja remover? ')
valores = [id]
sql = 'delete from informacao where id = ?'
cursor.execute(sql, valores)
conexao.commit()
conexao.clorse()