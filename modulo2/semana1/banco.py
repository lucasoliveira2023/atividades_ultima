import sqlite3
con = sqlite3.connect('banco.sqlite3')
cursor = con.cursor()
sql = '''
create table categoria (
    id integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    descricao text(100)
)
'''
cursor.execute(sql)
con.commit()
con.close()