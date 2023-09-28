list = []
list.append(1)
list.append(2)
list.append(3)
print(list[0])
print(list[1])
print(list[2])


print('#' *3)
for item in list:
    print(f'Lista no index {list.index(item)} é {item}')
    
    
lista = ['u', 'l', 't', 'i', 'm']
print(lista[:-1])
lista.pop()
lista.append('u')
print(lista)

dicionario = {'nome:': 'john:', 'lastname:': 'Doe'}
print(len(dicionario))
print(dicionario['nome:'])
print(dicionario['lastname:'])
dicionario['idade'] = 40
print(len(dicionario))
print(dicionario)
print('#' * 10)
print(type(dicionario.values()))
print(dicionario.values()) 
for valor in dicionario.values():
    print(f'valor é {valor}')
