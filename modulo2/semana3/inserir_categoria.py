import sqlite3

con = sqlite3.connect('banco.sqlite3')

cursor = con.cursor()

descricao = input("digite a categoria da descricao")

sql = 'insert into categoria (descricao) values (?)'

valores = [descricao]

cursor.execute(sql, valores)

con.commit()
con.close()