class PedidoService:

    @staticmethod
    def calcular_desconto(total):
        if total > 100:
            return total * 0.1
        return 0

    @classmethod
    def fechar_pedido(cls, pedido):
        total = pedido.total()
        desconto = cls.calcular_desconto(total)
        total_final = total - desconto

        return {
            "total": total,
            "desconto": desconto,
            "total_final": total_final
        }