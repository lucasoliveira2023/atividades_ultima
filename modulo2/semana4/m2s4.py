import sqlite3
import datetime

#função para criar a tabela todos
def criar_tabela_todos():
    conexao = sqlite3.connect('todo_app.db')
    cursor = conexao.cursor()
    cursor.execute(''' 
                   CREATE TABLE IF NOT EXISTS todos
                   (id INTERGER PRIMARY KEY AUTOINCREMENT,
                   descricao TEXT NOT NULL,
                   categoria_id INTERGE NOT NULL,
                   concluido INTERGE DEFAULT 0,
                   data_criacao DATE DEFAULT CURRENT_DATE,
                   data_conclusao DATE)
                   ''')
    conexao.commit()
    conexao.close()
    
    
#função para criar um todo
def criar_todo():
    descrissao = input("digite a descrissão do TODO:")
    categoria_id = int(input("digite o id da categoria:"))
    conexao =sqlite3.connect('todo_app.db')
    cursor =conexao.cursor()
    cursor.execute("INSERT INTO todos (descrissao, categoria_id) VALUES (?, ?, ?)", (descrissao, categoria_id))
    conexao.commit()
    print("TODO criado com sucesso!")
    conexao.close()
    
def atualizar_todo():
    todo_id = int(input("digite o id do TODO a ser atualizado"))
    descrissao = input("digite a nova descrissao do TODO:")
    concluido =int(input("digite 1 caso concluido,  ou 0 caso contrario:"))
    conexao = sqlite3.connect('todo_app.db')
    cursor = conexao.cursor()
    cursor.execute("UPDATE todos SET descrissao = ?, concluido = ? WHERE id = ?", (descrissao, concluido, todo_id))
    conexao.commit()
    print("TODO atualizado com sucesso!")
    conexao.close()
    
    
#função para excluir um todo
def excluir_todo():
    todo_id = int(input("Digite o ID do todo a ser excluido:"))
    conexao = sqlite3.connect('todo_app.db')
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM todos WHERE id = ?",(todo_id))
    conexao.commit()
    print("TODO excluido com sucesso!")
    conexao.close()
    
#função para criar uma categoria
def criar_categoria():
    nome = (input("digite o nome da categoria:"))
    conexao = sqlite3.connect('todo_app.db')
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO categorias (nome) VALUES (?)", (nome,))
    conexao.commit()
    print("categoria criada com sucesso")
    conexao.close()
    
#função para atualizar categoria
def atualizar_categoria():
    categoria_id = int(input("Digite o ID da categoria a ser atualizada:"))
    nome = input("Digite o novo nome da categoria:")
    conexao = sqlite3.connect('todo_app.db')
    cursor = conexao.cursor()
    cursor.execute("UPDATE categoria SET nome = ? WHERE id = ?", (nome, categoria_id))
    conexao.commit()
    print("categoria atualizada com sucesso")
    conexao.close()
    
#função para excluir categoria
def excluir_categoria():
    categoria_id = int(input("Digite o ID da categoria a ser excluida:"))
    conexao = sqlite3.connect('todo_app.db')
    cursor = conexao.cursor()
    conexao.commit()
    print("Categoria exluida com sucesso!")
    conexao.close()
    
#função para listar todos os afazeres de um dia especifico
def lista_afazeres_por_data():
    data = input("digite a data no formato yy-mm-dd:")
    conexao = sqlite3.connect('todo_app.db')
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM todos WHERE data_criacao = ?", (data,))
    todos =  cursor.fetchall()
    if todos:
        print("Afazeres do dia", data + ":")
        for todo in todos:
            print(f"ID: {todo[0]}, Descrição: {todo[1]}, Concluido: {todo[3]},")
    else:
        print("nenhum afazer para essa data")
    conexao.close()
    
#função para listar categoria
def lista_categorias():
    conexao = sqlite3.connect('todo_app.db')
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM categorias")
    categorias = cursor.fetchall()
    if categorias:
        print("Lista de Categorias:")
        for categoria in categorias:
            print(f"ID: {categoria[0]}, Nome: {categoria[1]}")
    else:
        print("nenhuma categoria encontrada.")
    conexao.close()
    
#função para marcar uma tarefa como concluida
def marca_tarefa_concluida():
    todo_id = int(input("Digite o ID do TODO a ser marcado como concluido:"))
    data_conclusao = datetime.date.today().strftime("%Y-%m-%d")
    conexao = sqlite3.connect('todo_app.db')
    cursor = conexao.cursor()
    cursor.execute("UPDATE todos Set concluido = 1, data_cnclusao = ? WHERE id = ?", (data_conclusao, todo_id))
    conexao.commit()
    print("Tarefa marcada como concluida com sucesso!")
    
#funçao principal para executar o programa
def main():
    criar_tabela_todos()
    criar_categoria()
    
    while True:
        print("\n=== Aplicação CLI TODO ===")
        print("1. criar TODO")
        print("2. ATUALIZAR TODO")
        print("3. Excluir TODO")
        print("4. Criar categoria")
        print("5. Atualizar categoria")
        print("6. Excluir categoria")
        print("7. Lista afazeres de um dia específico")
        print("8. Listar todas as categorias")
        print("9. Marcar tarefa como concluida")
        print("0, Sair")
        
        
        opcao = input("Digite o número da opção desejada:")
        
        if opcao == "1":
            criar_todo()
        elif opcao == "2":
            atualizar_todo()
        elif opcao == "3":
            excluir_todo()
        elif opcao == "4":
            criar_categoria()
        elif opcao == "5":
            atualizar_categoria()
        elif opcao == "6":
            excluir_categoria()
        elif opcao == "7":
            lista_afazeres_por_data()
        elif opcao == "8":
            lista_categorias()
        elif opcao == "9":
            marca_tarefa_concluida()
        elif opcao == "0":
            print("Saindo da aplicação")
            break
        else:
            print("opção invalida.Digite um número válido. ")
            
if __name__ == '__main__':
    main()