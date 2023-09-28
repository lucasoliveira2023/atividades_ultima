#Crie um programa em Python que gere tabelas para uma aplicação de
# gerenciamento de tarefas.
# As tabelas devem compreender as seguintes funcionalidades:
#As tarefas devem ser divididas em “categorias”;
#Uma tarefa deve ter nome, data, categoria e status
# de conclusão (se foi realizada ou não); 
#As restrições/relacionamentos devem fazer sentido

class Tarefa:
    def __init__(self, nome, data, categoria, status):
        self.nome = nome
        self.data = data
        self.categoria = categoria
        self.status = status
        
        
class GerenciadorDeTarefas:
    def __init__(self):
        self.tarefas = []
        
    def adicionar_tarefa(self, tarefa):
        self.tarefas.append(tarefa)
        
    def tarefas_por_categorias(self, categoria):
        tarefa_por_categoria = []
        for tarefa in self.tarefas:
            if tarefa.categoria == categoria:
                tarefa_por_categoria.append(tarefa)
        return tarefa_por_categoria
    
    def tarefas_por_status(self, status):
        tarefa_por_status = []
        for tarefa in self.tarefas:
            if tarefa.status == status:
                tarefa_por_status.append(tarefa)
        return tarefa_por_status
        
def gerar_tabelas_de_tarefas(tasks):
    tabela = []
    tabela.append(["NOME", "DATA", "CATEGORIA", "STATUS"])
    for task in tasks:
        tabela.append([task.nome, task.data, task.categoria, task.status])
    return tabela

gerenciador = GerenciadorDeTarefas()
tarefa1 = Tarefa("fazer atividade do M2 S2", "2023-06-23", "Estudos", "Em andamento")
tarefa2 = Tarefa("fazer compras", "2023-06-22", "compras", "Pendente")
tarefa3 = Tarefa("arrumar o quarto", "2023-06-21", "organização", "Concluido")


gerenciador.adicionar_tarefa(tarefa1)
gerenciador.adicionar_tarefa(tarefa2)
gerenciador.adicionar_tarefa(tarefa3)

tarefas_por_categoria = gerenciador.tarefas_por_categorias("Estudos")
for tarefa in tarefas_por_categoria:
    print("Nome:", tarefa.nome)
    print("Data:", tarefa.data)
    print("Categoria:", tarefa.categoria)
    print("Status:", tarefa.status)
    print()
    
tarefas_status = gerenciador.tarefas_por_status("Pendente")
for tarefa in tarefas_status:
    print("Nome:", tarefa.nome)
    print("Data:", tarefa.data)
    print("Categoria:", tarefa.categoria)
    print("Status:", tarefa.status)
    print()
    
tabelas_de_tarefas = gerar_tabelas_de_tarefas(gerenciador.tarefas)
for row in tabelas_de_tarefas:
    print("\t".join(row))