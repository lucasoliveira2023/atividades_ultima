import sqlite3
import hashlib

con = sqlite3.connect('banco.sqlite4')
cursor = con.cursor()

nome =  input("digite o seu nome: ")
email =  input("digite seu email: ")
while True:
    senha = input("Digite sua senha: ")
    confirma_senha = input("confirme sua senha: ")
    if senha == confirma_senha:
        break
    else:
        print("a confimacao de senha está errada!")
        
sql = 'insert into usuario (nome, email, senha) values (?, ?, ?)'

senha =hashlib.sha256(senha.encode('utf-8')).hexdigest()
valores = [nome, email, senha]
cursor.execute(sql, valores)
con.commit()
con.close()