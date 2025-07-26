from database.connection import conectar
import mysql.connector

class ClienteModel:
    def __init__(self):
        self.conn = conectar()
        self.cursor = self.conn.cursor()

    def salvar_cliente(self, nome, email, telefone, endereco):
        try:
            query = "INSERT INTO clientes (nome, email, telefone, endereco) VALUES (%s, %s, %s, %s)"
            values = (nome, email, telefone, endereco)
            self.cursor.execute(query, values)
            self.conn.commit()
        except mysql.connector.Error as err:
            print(f"Erro ao salvar cliente: {err}")
        finally:
            self.cursor.close()
            self.conn.close()

    def listar_clientes(self):
        try:
            query = "SELECT * FROM clientes"
            self.cursor.execute(query)
            return self.cursor.fetchall()
        except mysql.connector.Error as err:
            print(f"Erro ao listar clientes: {err}")
        finally:
            self.cursor.close()
            self.conn.close()
