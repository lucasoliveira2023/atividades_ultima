from random import randint
number = randint(1, 100)
tentativas = 5
while tentativas > 0:
    chute = int(input("digite o chute:"))
    diferenca = number - chute
    if diferenca == 0:
        print("vc acertou!")
        break
    elif diferenca <= 5  and diferenca >+ -5:
        print("vc errou, mas is worm")
    elif diferenca > 0:
        print("vc errou o numero era maior")
    else:
        print("vc errou o numero era menor")
    tentativas = tentativas - 1
print("and the real number is:", number)