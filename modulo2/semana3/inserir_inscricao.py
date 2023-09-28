import sqlite3
con = sqlite3.connect('banco.sqlite3')
cursor = con.cursor()

sql = 'select id, descricao, data from evento'

eventos = cursor.execute(sql)

for evento in eventos:
    print("ID:", evento[0], "Descricao:", evento[1], "Data:", evento[2])
    
evento_id = input("digite o id do evento desejado:")
nome = input("digite o seu nome:")
email = input("digite o seu email:")

sql = 'insert into incricao (evento_id, nome, email) values (?, ?, ?)'
sql = "insert into incricao (evento_id, nome, email) values (1, 'fulano', fulano@email.com)"

valores = [evento_id, nome, email]

cursor.execute(sql, valores)