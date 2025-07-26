import bcrypt
from app.database.connection import get_connection

class Usuario:
    def __init__(self, id, nome, login, senha_hash, nivel_acesso):
        self.id = id
        self.nome = nome
        self.login = login
        self.senha_hash = senha_hash
        self.nivel_acesso = nivel_acesso

    @staticmethod
    def verificar_senha(senha, senha_hash):
        return bcrypt.checkpw(senha.encode('utf-8'), senha_hash.encode('utf-8'))