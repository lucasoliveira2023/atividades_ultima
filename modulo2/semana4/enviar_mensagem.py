import sqlite3
import datetime

from autenticar import validar_login

con = sqlite3.connect('banco.sqlite4')
cursor = con.cursor()
try:
    usuario = validar_login(cursor)
except Exception as ex:
    print(ex)
    exit()
    
mensagem = input("Digite sua mensagem: ")
hoje = datetime.date.today()
hoje = hoje.strftime('%Y-%m-%d')

sql = 'insert into mensagem (usuario_id, texto, data) values (?, ?, ?)'

valores = [usuario [0], mensagem, hoje]

cursor.execute(sql, valores)
con.commit()
con.close()