import socket

HOST = "127.0.0.1"
PORT = 9000
print("iniciando o socket")
s = socket.socket()
print("CONECTANDO COM O SERVIDOR ")
s.connect((HOST, PORT))
numero1 = input("Digite um numero:")
numero2 = input("Digite um numero:")
texto = f'{numero1}x{numero2}'
print(f"ENVIANDO O TEXTO: {texto}")
s.sendall(texto.encode("utf-8"))
dados = s.recv(1024)
s.close()
texto = dados.decode("utf-8")
print(f"Cliente: Recebi {texto}")