import sqlite3
conexao = sqlite3.connect('m2s4dados.sqlite30')


id = input('Qual o ID deseja alterar? ')
atividades = input('Informe o sua atividade: ')
diario_id = input('''
Informe o dia da semana:
[1] Segunda
[2] Terça
[3] Quarta 
[4] Quinta
[5] Sexta
''')
tarefas_id = input('''
Informe o dias das suas tarefas:
[1] Segunda
[2] Terça
[3] Quarta 
[4] Quinta
[5] Sexta ''' )

sql = 'update informacao set atividades = ?, diario_id = ?, tarefas_id = ? where id ?'  
valores = [id, atividades, diarios_id, tarefas_id]
cursor.execute(sql, valores)
conexao.commit()
conexao.close()