from app.database.connection import conectar
import mysql.connector

class ProdutoModel:
    def __init__(self):
        self.conn = conectar()
        self.cursor = self.conn.cursor()

    def salvar_produto(self, nome, descricao, preco):
        try:
            query = "INSERT INTO produtos (nome, descricao, preco) VALUES (%s, %s, %s)"
            values = (nome, descricao, preco)
            self.cursor.execute(query, values)
            self.conn.commit()
        except mysql.connector.Error as err:
            print(f"Erro ao salvar produto: {err}")
        finally:
            self.cursor.close()
            self.conn.close()

    def listar_produtos(self):
        try:
            query = "SELECT * FROM produtos"
            self.cursor.execute(query)
            return self.cursor.fetchall()
        except mysql.connector.Error as err:
            print(f"Erro ao listar produtos: {err}")
        finally:
            self.cursor.close()
            self.conn.close()
