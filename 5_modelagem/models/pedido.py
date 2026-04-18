from datetime import datetime

class Pedido:
    def __init__(self, usuario):
        self.usuario = usuario
        self.produtos = []
        self.data = datetime.now()

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def total(self):
        return sum(p.preco for p in self.produtos)

    def __str__(self):
        return f"Pedido de {self.usuario.nome} com {len(self.produtos)} produtos"