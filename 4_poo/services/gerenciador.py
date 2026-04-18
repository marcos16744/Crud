from models.tarefa import Tarefa

class GerenciadorTarefas:
    def __init__(self):
        self.tarefas = {}

    def adicionar(self, tarefa: Tarefa):
        if tarefa.id in self.tarefas:
            return "Já existe essa tarefa"

        self.tarefas[tarefa.id] = tarefa
        return "Tarefa cadastrada com sucesso"

    def mostrar(self, id):
        if id not in self.tarefas:
            return "Não existe"

        return self.tarefas[id].to_dict()
    
        