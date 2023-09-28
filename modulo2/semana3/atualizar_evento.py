import sqlite3

con = sqlite3.connect('banco.sqlite3')

cursor = con.cursor()

sql = 'select id, descricao, categoria_id, data from evento'
eventos = cursor.execute(sql)

for evento in eventos:
    print("ID:", evento[0], "Descricao:", evento[1], "Categoria ID:", evento[2], "Data:", evento[3])
    
evento_id = input("digite o id do evento que deseja atualisar:")

descricao = input("digite a nova descricao:")
data = input("digite a nova data:")

sql = 'update evento set descricao = ?, data = ?'

valores = [descricao, data]
cursor.execute(sql, valores)
con.commit()
con.close()