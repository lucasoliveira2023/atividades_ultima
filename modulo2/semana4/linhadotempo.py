import sqlite3 

from autenticar import validar_login

con = sqlite3.connect('banco.sqlite4')
cursor = con.cursor()

try:
    usuario = validar_login(cursor)
except Exception as ex:
    print(ex)
    exit()
    
sql = '''
select u.nome, m.texto, m.data from mensagem m inner join usuario u on m.usuario_id = 
u.id
where m.usuario_id in (select c.alvo_id from conexao c where c.usuario_id = ?) 
or m.usuario_id = ?
'''

valores = [usuario[0], usuario[0]]
consulta = cursor.execute(sql, valores)
for result in consulta:
    print('Nome:', result[0], 'Texto:', result[1], 'Data:', usuario[2])
    
con.close()