from random import randint
quant = int(input("digite a quantidade de dados"))
tipo_dado = int(input("digite o tipo de dado:"))
repeticao = int(input("digite quantas vezes:"))
tentativa = 1
valores = []
while tentativa <= repeticao:
    quant_temp = 1
    while quant_temp <+ quant:
        valor = randint(1, tipo_dado)
        print(valor)
        quant_temp = quant_temp + 1
        print("---terminou a repeticao---")
    tentativa = tentativa + 1
print("and")