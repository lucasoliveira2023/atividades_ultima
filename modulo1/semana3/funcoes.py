def meu_nome_func():
    control = False
    meu_nome = input("digite o nome", )
    if meu_nome == "lucas":
        control = True
    print("ola mundo, meu nome é:" )
    return control

retorno = meu_nome_func()
if retorno:
    print("nome valido")
else:
    print("nome invalido")
    
    
def soma_two_number(x, y):
    return x +y

def soma_number(*args):
    soma = 0
    for number in args:
        soma = soma + number
    return soma

result_soma= soma_two_number(1, 2)
print(result_soma)
soma_many_number = soma_number(1,2,3,4,5)
print(soma_many_number)


def descricao_livro(titulo, autor= 'Desconhecido'):
    print("o livro: {} autor: {}" .format(titulo,autor))
    
descricao_livro(autor="J.R Tolkien", titulo= "lord of the ring")
descricao_livro(titulo= "lord of the ring")

def descricao_livro2(**kwargs):
    for chave in kwargs:
        print(chave + ":" + kwargs[chave])
        
descricao_livro2(autor="J.R Tolkien", titulo="menino maluqinho", resumo= "Bla bla")