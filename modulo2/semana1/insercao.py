import sqlite3
con = sqlite3.connect('banco.sqlite3')
cursor = con.cursor()

sql = '''
insert into categoria (descricao) values ('celulares')

'''

cursor.execute(sql)
con.commit()
con.close()