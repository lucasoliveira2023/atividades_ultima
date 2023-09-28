#Crie um programa em Python que gere tabelas para uma aplicação de eventos.
# Elas devem compreender as seguintes funcionalidades:
#Eventos devem ter título, data e local, além da referência ao organizador;
#O organizador deve ter nome, email e cpf;
#As restrições/relacionamentos devem fazer sentido.
class Organizador:
    def __init__(self, nome, email, cpf):
        self.nome = nome
        self.email = email
        self.cpf = cpf
        

class Evento:
    def __init__(self, titulo, data, local, organizador):
        self.titulo = titulo
        self.data = data
        self.local = local
        self.organizador = organizador
        
        
def criar_evento():
    titulo = input("digite um titulo:")
    data = input("digite uma data")
    local = input("digite um local:")
    
    nome_organizador = (input("digite um nome:"))
    nome_email_organizador = (input("digite um email:"))
    numero_cpf = (input("digite um numero de cpf:"))
    
    organizador = Organizador(nome_organizador, nome_email_organizador, numero_cpf)
    evento = Evento(titulo, data, local, organizador)
    
    return evento


def exibir_eventos(evento):
    print("Titulo:", evento.titulo)
    print("Data:", evento.data)
    print("Local:", evento.local)
    print("Organizador:", evento.organizador.nome)
    print("Nome:", evento.organizador.nome)
    print("Email:", evento.organizador.email)
    print("Cpf:", evento.organizador.cpf)
    
    
evento1 = criar_evento()
print("exibir detalhes do evento 1:")
exibir_eventos(evento1)

evento2 = criar_evento()
print("exibir detalhes do evento 2:")
exibir_eventos(evento2)
