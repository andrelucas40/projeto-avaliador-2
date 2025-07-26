from app.models.usuario import Usuario
from app.database.connection import get_connection

class UsuarioController:
    def __init__(self):
        self.conn = get_connection()

    def autenticar(self, login, senha):
        cursor = self.conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM usuarios WHERE login = %s", (login,))
        usuario = cursor.fetchone()
        if usuario and Usuario.verificar_senha(senha, usuario['senha_hash']):
            return usuario
        return None
