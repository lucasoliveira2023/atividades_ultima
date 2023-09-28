def mostrar(func):
    def interno():
        print("o usuario atual é :", end="")
        func()
    return interno

def quem():
    print("Alice")
    

myobj = mostrar(quem)
myobj()