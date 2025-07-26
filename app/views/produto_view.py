import tkinter as tk
from tkinter import messagebox
from app.controllers.produto_controller import ProdutoController

class ProdutoView:
    def __init__(self, root):
        self.controller = ProdutoController()
        self.root = root
        self.root.title("Produtos")

        self.frame = tk.Frame(root)
        self.frame.pack()

        tk.Label(self.frame, text="Nome").grid(row=0, column=0)
        self.entry_nome = tk.Entry(self.frame)
        self.entry_nome.grid(row=0, column=1)

        tk.Label(self.frame, text="Preço").grid(row=1, column=0)
        self.entry_preco = tk.Entry(self.frame)
        self.entry_preco.grid(row=1, column=1)

        tk.Label(self.frame, text="Estoque").grid(row=2, column=0)
        self.entry_estoque = tk.Entry(self.frame)
        self.entry_estoque.grid(row=2, column=1)

        self.btn_add = tk.Button(self.frame, text="Adicionar", command=self.adicionar_produto)
        self.btn_add.grid(row=3, columnspan=2)

    def adicionar_produto(self):
        nome = self.entry_nome.get()
        preco = float(self.entry_preco.get())
        estoque = int(self.entry_estoque.get())
        self.controller.criar_produto(nome, preco, estoque)
        messagebox.showinfo("Sucesso", "Produto adicionado com sucesso!")
        self.entry_nome.delete(0, tk.END)
        self.entry_preco.delete(0, tk.END)
        self.entry_estoque.delete(0, tk.END)
