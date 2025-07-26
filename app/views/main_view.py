import tkinter as tk

class MainView:
    def __init__(self, master):
        self.master = master
        master.title("Sistema de Loja")

        tk.Button(master, text="Vendas", command=self.abrir_vendas).pack(pady=10)
        tk.Button(master, text="Produtos", command=self.abrir_produtos).pack(pady=10)
        tk.Button(master, text="Clientes", command=self.abrir_clientes).pack(pady=10)

    def abrir_vendas(self):
        import tkinter as tk
        from app.controllers.venda_controller import VendaController
        from app.views.venda_view import VendaView
        top = tk.Toplevel(self.master)
        VendaView(top, VendaController())

    def abrir_produtos(self):
        pass  # Para implementar

    def abrir_clientes(self):
        pass  # Para implementar
