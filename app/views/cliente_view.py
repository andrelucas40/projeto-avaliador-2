import tkinter as tk

class ClienteView:
    def __init__(self, root, controller):
        self.controller = controller

        # Layout
        self.frame = tk.Frame(root)
        self.frame.pack()

        self.label_nome = tk.Label(self.frame, text="Nome do Cliente:")
        self.label_nome.grid(row=0, column=0)
        self.nome_entry = tk.Entry(self.frame)
        self.nome_entry.grid(row=0, column=1)

        self.label_email = tk.Label(self.frame, text="Email do Cliente:")
        self.label_email.grid(row=1, column=0)
        self.email_entry = tk.Entry(self.frame)
        self.email_entry.grid(row=1, column=1)

        self.cadastrar_button = tk.Button(self.frame, text="Cadastrar Cliente", command=self.cadastrar_cliente)
        self.cadastrar_button.grid(row=2, columnspan=2)

    def cadastrar_cliente(self):
        nome = self.nome_entry.get()
        email = self.email_entry.get()
        self.controller.cadastrar_cliente(nome, email)
