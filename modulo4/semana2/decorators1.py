def ola(func):
    def inner():
        print("Olá")
        func()
        print("tudo bem")
    return inner

def name():
    print("Alice")
    
print("Antes")
variavel_obj = ola(name)
print("Depois")
variavel_obj()
print("Final")
