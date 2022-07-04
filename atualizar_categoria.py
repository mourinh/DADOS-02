import sqlite3
conexao = sqlite3.connect('m2s4dados.sqlite3')

sql = '''
UPDATE informacao SET atividades = assistir netflix WHERE id = 2
'''
cursor.execute(sql)
conexao.commit()
conexao.close()