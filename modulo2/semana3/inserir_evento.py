import sqlite3

con = sqlite3.connect('banco.sqlite3')

cursor = con.cursor()

descricao = input("qual a descricao do evento:")
data = input("qual a data do envento:")

sql = 'select id, descricao from categoria'
categorias = cursor.execute(sql)
print("categorias diasponiveis:")
for categoria in categorias:
    print("ID:", categoria[0], "Descricao", categoria[1])
    
categoria_id = input("digite o ID da categoria desejada:")

sql = 'insert into evento (descricao, data, categoria_id) values (?, ?, ?)'

valores = [descricao, data, categoria_id]

cursor.execute(sql, valores)

con.commit()
con.close()