import tkinter as tk
from tkinter import messagebox


class LoginView:
    def __init__(self, master, controller):
        self.master = master
        self.controller = controller
        master.title("Login")

        tk.Label(master, text="Login:").grid(row=0, column=0)
        self.login_entry = tk.Entry(master)
        self.login_entry.grid(row=0, column=1)

        tk.Label(master, text="Senha:").grid(row=1, column=0)
        self.senha_entry = tk.Entry(master, show='*')
        self.senha_entry.grid(row=1, column=1)

        tk.Button(master, text="Entrar", command=self.login).grid(row=2, column=0, columnspan=2)

    def login(self):
        login = self.login_entry.get()
        senha = self.senha_entry.get()
        usuario = self.controller.autenticar(login, senha)
        if usuario:
            messagebox.showinfo("Sucesso", f"Bem-vindo, {usuario['nome']}!")
            self.master.destroy()
            import app.views.main_view as mv
            root = tk.Tk()
            mv.MainView(root)
            root.mainloop()
        else:
            messagebox.showerror("Erro", "Login ou senha inválidos")
