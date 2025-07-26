from app.database.connection import get_connection

class ItemVenda:
    def __init__(self, id, venda_id, produto_id, quantidade, preco_unitario):
        self.id = id
        self.venda_id = venda_id
        self.produto_id = produto_id
        self.quantidade = quantidade
        self.preco_unitario = preco_unitario