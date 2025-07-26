from app.models.venda import Venda
from app.models.item_venda import ItemVenda
from app.database.connection import get_connection

class VendaController:
    def __init__(self):
        self.conn = get_connection()

    def registrar_venda(self, cliente_id, usuario_id, itens):
        cursor = self.conn.cursor()
        total = sum(item['quantidade'] * item['preco_unitario'] for item in itens)

        cursor.execute("""
            INSERT INTO vendas (cliente_id, usuario_id, total)
            VALUES (%s, %s, %s)
        """, (cliente_id, usuario_id, total))
        venda_id = cursor.lastrowid

        for item in itens:
            cursor.execute("""
                INSERT INTO itens_venda (venda_id, produto_id, quantidade, preco_unitario)
                VALUES (%s, %s, %s, %s)
            """, (venda_id, item['produto_id'], item['quantidade'], item['preco_unitario']))

        self.conn.commit()
        return venda_id

    def listar_vendas(self):
        cursor = self.conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM vendas")
        return cursor.fetchall()