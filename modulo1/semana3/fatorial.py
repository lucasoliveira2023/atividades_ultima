def fatorial(number):
    print("chamada co parametro", number)
    if number == 1:
        return 1
    return number * fatorial(number-1)

retorno = fatorial(3)

print(retorno)