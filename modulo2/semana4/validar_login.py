import sqlite3
import hashlib

con = sqlite3.connect('banco.sqlite4')
cursor = con.cursor()

email = input("digite email: ")
senha = input("digite senha: ")

sql ='select count(1) from usuario where email = ? and senha = ?'

senha = hashlib.sha256(senha.encode('utf-8')).hexdigest()

valores = [email, senha]
consulta = cursor.execute(sql, valores)

existe = 0
for result in consulta:
    existe =result[0]

if existe > 0:
    print("usuario existe!")
else:
    print("usuario não existe!")