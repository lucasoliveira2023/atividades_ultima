def decorator_imprimir(funcao):
    def fees(capital, tax, time):
        result = funcao(capital, tax, time)
        print(f"parametro: Capital: {capital}, tax: {tax}, time: {time}")
        return result
    return fees

@decorator_imprimir
def simple_fee(capital, tax, time): 
    fees = capital * tax * time
    return fees

result = simple_fee(1000, 0.05, 2)
print(result)