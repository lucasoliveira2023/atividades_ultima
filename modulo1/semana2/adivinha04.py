from random import randint
number = randint(1, 10)
tentativas = 5
while tentativas > 0:
    chute = int(input("digite seu chute:"))
    if chute == number:
        print("parabens vc acertou!")
        break
    elif chute < number:
        print("vc errou o numero era maior")
    else:
        print("vc errou o numero era menor")
    tentativas = tentativas -1
print("and")