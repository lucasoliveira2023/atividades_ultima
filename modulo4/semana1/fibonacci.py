class Fibonacci:
    
    def __init__(self,maximo):
        self.elemento_atual = 0
        self.prox_elemento = 1
        self.maximo = maximo
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.elemento_atual > self.maximo:
            raise StopIteration
        
        valor_retorno = self.elemento_atual
        self.elemento_atual, self.prox_elemento = self.prox_elemento, self.elemento_atual + self.prox_elemento
        
        
        return valor_retorno
    
    def __str__(self):
        return f"Fibonaccci de  {self.maximo} atual -> {self.elemento_atual} proximo -> {self.prox_elemento}"
    


obj_fibonnacci = Fibonacci(10)
print(obj_fibonnacci)
for numero in obj_fibonnacci:
    print(numero)
print("final da iteracao")