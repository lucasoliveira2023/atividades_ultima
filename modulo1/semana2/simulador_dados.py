from random import randint
quant = int(input("digite a quantidade de dados:"))
tentativa = 1
valores = []
while tentativa <= quant:
    valor = randint(1, 6)
    print(valor)
    valores.append(valor)
    tentativa = tentativa + 1
print("total:", sum(valores))
print("media:", sum(valores)/quant)
print("maior:", max(valores))
print("menor", min(valores))
print("and")