class Tarefa:
    def __init__(self, id, titulo, descricao, status, data_criacao):
        self.id = id
        self.titulo = titulo
        self.descricao = descricao
        self.status = status
        self.data_criacao = data_criacao

    def to_dict(self):
        return {
            "id": self.id,
            "titulo": self.titulo,
            "descricao": self.descricao,
            "status": self.status,
            "data_criacao": self.data_criacao
        }
    
