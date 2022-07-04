import sqlite3
conexao = sqlite3.connect('m2s4dados.sqlite3')

sql = '''
DELETE FROM informacao WHERE id = 3;
'''
cursor.execute(sql)
conexao.commit()
conexao.close()
