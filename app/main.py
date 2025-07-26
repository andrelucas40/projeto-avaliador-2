from tkinter import Tk
from app.controllers.usuario_controller import UsuarioController
from app.views.login_view import LoginView

def main():
    from tkinter import messagebox
    root = Tk()
    
    try:
        controller = UsuarioController()
        print("Controller OK!")
    except Exception as e:
        print("Erro ao carregar o controller:", e)
        messagebox.showerror("Erro", f"Erro ao conectar com o banco: {e}")
        return

    LoginView(root, controller)
    root.mainloop()
