from models.cliente_model import ClienteModel

class ClienteController:
    def __init__(self):
        self.cliente_model = ClienteModel()

    def cadastrar_cliente(self, nome, email, telefone, endereco):
        if nome and email:
            self.cliente_model.salvar_cliente(nome, email, telefone, endereco)
            print(f"Cliente {nome} cadastrado com sucesso!")
        else:
            print("Erro: dados inválidos.")

    def listar_clientes(self):
        return self.cliente_model.listar_clientes()
