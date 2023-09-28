from random import randint

number = randint(1, 2)

chute = int(input("digite seu chute:"))

if chute == number:
    print("parabens vc acertou")
else:
    print("voce errou, o numero era:", number)
    
print("AND")