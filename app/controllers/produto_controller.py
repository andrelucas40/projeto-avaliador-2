from app.models.produto_model import ProdutoModel
class ProdutoController:
    def __init__(self):
        self.produto_model = ProdutoModel()

    def cadastrar_produto(self, nome, descricao, preco):
        if nome and preco:
            self.produto_model.salvar_produto(nome, descricao, preco)
            print(f"Produto {nome} cadastrado com sucesso!")
        else:
            print("Erro: dados inválidos.")

    def listar_produtos(self):
        return self.produto_model.listar_produtos()
