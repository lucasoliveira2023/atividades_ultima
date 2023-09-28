def calcular_soma(*args):
    soma = sum(args)
    return soma

numeros = []
numero = 0 

#lendo os numeros de entrada até que o menos 1 seja recebido
while numero != -1:
    numero = int (input())
    if numero != -1:
        numeros.append(numero)
        
#chamar a função e obter o resultado da soma
resultado = calcular_soma(*numeros)

print(resultado)