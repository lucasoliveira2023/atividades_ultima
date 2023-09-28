from random import randint

number = randint(1, 10)

chute = int(input("digite seu chute"))

if chute == number:
    print("parabens vc acertou")
elif chute < number:
    print("errou o numero era maior")
else:
    print("parabens errou o numero era menor")
    
print("FIM DO PROGRAMA")