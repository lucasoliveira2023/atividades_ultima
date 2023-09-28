import sqlite3

con = sqlite3.connect('banco.sqlite3')

cursor = con.cursor()

sql = 'select id, descricao, categoria_id, data from evento'

eventos = cursor.execute(sql)
print("Eventos disponiveis:")
for evento in eventos:
    print("ID:", evento[0], 'Descricao', evento [1], 'Categoria:', evento[2], 'Data:', evento[3])
    
evento_id = input("digite o id do evento a se apagar:")

sql = 'delete from where id = ?'

valores = [evento_id]
cursor.execute(sql, valores)
con.commit()
con.close()