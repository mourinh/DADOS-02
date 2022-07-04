import sqlite3
conexao = sqlite3.connect('m2s4dados.sqlite3')
sql = '''select * from informacao where diarios_id like '1%' '''
consulta = cursor.execute(sql)
for resultado in consulta: 
    print(resultado)