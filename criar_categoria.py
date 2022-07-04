import sqlite3
conexao = sqlite3.connect('m2s4dados.sqlite3')

sql = sql = ''' 
INSERT INTO fornecedores (id, atividades, diarios_id, tarefas_id) 
VALUES (4, 'Academia', '1', '1');
'''

cursor.execute(sql)
conexao.commit()
conexao.close()