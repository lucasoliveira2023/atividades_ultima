def formata_romano(letra, repeticao):
    return str(letra*repeticao)

def convercao(numero):
    lista = ["I", "V", "X"]
    
    if numero <+ 3:
        return formata_romano(lista[0])
    elif numero == 4:
        return "IV"
    elif numero >=  5 or numero < 9:
        repetir = numero -5
        return "V"
    elif numero % 10 == 0 and int(numero/10) <= 3:
        repetir = int(numero/10)
        return formata_romano(lista[2], repetir)
    
##########################################################################################
numero = int(input("digite o numero: "))

numero_romano = convercao(numero)
print("numero em romano", numero_romano)