from models.usuario import Usuario
from models.produto import Produto
from models.pedido import Pedido
from services.pedido_service import PedidoService
from utils.formatador import Formatador

# criando usuário
user = Usuario("Marcos", "marcos@email.com")

# criando produtos
p1 = Produto("Teclado", 50)
p2 = Produto("Mouse", 70)

# criando pedido
pedido = Pedido(user)
pedido.adicionar_produto(p1)
pedido.adicionar_produto(p2)

# usando service
resultado = PedidoService.fechar_pedido(pedido)

print("Total:", Formatador.moeda(resultado["total"]))
print("Desconto:", Formatador.moeda(resultado["desconto"]))
print("Final:", Formatador.moeda(resultado["total_final"]))