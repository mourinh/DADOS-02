import sqlite3
conexao = sqlite3.connect('m2s4dados.sqlite3')
cursor = conexao.cursor()

id = input('Adicione o ID para atividade: ')
atividade = input('Adicione sua atividade do dia: ')
diario_id = input('''
Adicione o dia dos dias da semana:
[1] Segunda
[2] Terça
[3] Quarta 
[4] Quinta
[5] Sexta
''')
tarefas_id = input('Coloca os dias da semana: ')

sql = 'INSERT INTO informacao (id, atividade, diario_id, tarefas_id) VALUE (?, ?, ?, ?)'
valores = [id, atividade, diario_id, tarefas_id]
cursor.execute(sql, valores)
conexao.commit()
print ('DADOS FEITO COM SUCESSO!')
conexao.close()

