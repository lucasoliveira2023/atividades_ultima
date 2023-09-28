clientes = []

for cliente in range(5):
    nome = input()
    cpf = input()
    idade = input()
    
    cadastro_atual = {}
    cadastro_atual['Nome'] = nome
    cadastro_atual["CPF"] = cpf
    cadastro_atual["idade"] = idade
    clientes.append(cadastro_atual) 
    
for cliente in clientes:
    print("Cliente:", cliente["Nome"], "CPF:", cliente["CPF"], "Idade:", cliente["Idade"])