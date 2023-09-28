def mostrar(func):
    def inner():
        print("o usuario atual é:", end='')
        func()
    return inner

@mostrar
def quem():
    print("Alice")

@mostrar
def send_email_system(texto):
    print("Sending email")
    
#if __name__ == '__main__':
    quem()