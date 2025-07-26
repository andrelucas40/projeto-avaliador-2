from app.database.connection import get_connection

class Venda:
    def __init__(self, id, cliente_id, usuario_id, data, total):
        self.id = id
        self.cliente_id = cliente_id
        self.usuario_id = usuario_id
        self.data = data
        self.total = total

    @staticmethod
    def buscar_por_id(venda_id):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM vendas WHERE id = %s", (venda_id,))
        return cursor.fetchone()
