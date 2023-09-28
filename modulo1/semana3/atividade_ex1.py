def par_impar(number):
    if number % 2 == 0:
        return "Par"
    else:
        return "Impar"
    
num = int(input())
print(par_impar(num))