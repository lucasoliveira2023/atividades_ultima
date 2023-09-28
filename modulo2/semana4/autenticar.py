import hashlib

def validar_login(cursor):
    email = input("digite email: ")
    senha = input("digite a senha: ")
    
    sql = 'select id, nome, senha from usuario where email = ? and senha = ?'
    
    senha = hashlib.sha256(senha.encode('utf-8')).hexdigest()
    
    valores = [email, senha]
    consulta = cursor.execute(sql, valores)
    
    usuario = None
    for result in consulta:
        usuario = result
        break
    
    if usuario is None:
        raise Exception('Email ou senha invalidos!')
    return usuario