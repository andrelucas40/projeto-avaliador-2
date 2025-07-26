import tkinter as tk
from tkinter import messagebox

class VendaView:
    def __init__(self, master, controller):
        self.master = master
        self.controller = controller
        master.title("Registrar Venda")

        self.cliente_id_entry = tk.Entry(master)
        self.usuario_id_entry = tk.Entry(master)
        self.itens_entry = tk.Entry(master)

        tk.Label(master, text="Cliente ID:").pack()
        self.cliente_id_entry.pack()

        tk.Label(master, text="Usuário ID:").pack()
        self.usuario_id_entry.pack()

        tk.Label(master, text="Itens (formato: produto_id,quantidade,preco|...):").pack()
        self.itens_entry.pack()

        tk.Button(master, text="Registrar", command=self.registrar).pack(pady=10)

    def registrar(self):
        try:
            cliente_id = int(self.cliente_id_entry.get())
            usuario_id = int(self.usuario_id_entry.get())
            itens_str = self.itens_entry.get()

            itens = []
            for item_str in itens_str.split('|'):
                pid, qtd, preco = item_str.split(',')
                itens.append({
                    'produto_id': int(pid),
                    'quantidade': int(qtd),
                    'preco_unitario': float(preco)
                })

            venda_id = self.controller.registrar_venda(cliente_id, usuario_id, itens)
            messagebox.showinfo("Sucesso", f"Venda registrada! ID: {venda_id}")
        except Exception as e:
            messagebox.showerror("Erro", str(e))
