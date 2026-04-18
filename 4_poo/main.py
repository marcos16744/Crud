from services.gerenciador import GerenciadorTarefas
from models.tarefa import Tarefa

gerenciador = GerenciadorTarefas()

while True:
    print("\n1 - Adicionar tarefa")
    print("2 - Mostrar tarefa")
    print("0 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        id = input("ID: ")
        titulo = input("Título: ")
        descricao = input("Descrição: ")
        status = input("Status: ")
        data = input("Data: ")

        tarefa = Tarefa(id, titulo, descricao, status, data)
        print(gerenciador.adicionar(tarefa))

    elif opcao == "2":
        id = input("ID: ")
        print(gerenciador.mostrar(id))

    elif opcao == "0":
        break


