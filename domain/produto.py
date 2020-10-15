from domain.domain_exception import DomainException
from domain.categoria import Categoria


class Produto:
    def __init__(self, nome: str, quantidade: int, preco: float, categoria: Categoria):
        self.validar(nome, quantidade, preco, categoria)
        self.nome = nome
        self.quantidade = quantidade
        self.preco = preco
        self.categoria = categoria

    def validar(self, nome, quantidade, preco, categoria):
        DomainException()\
            .quando_vazio(nome, "O nome é um campo obrigatório")\
            .quando_vazio(quantidade, "A quantidade é um campo obrigatório")\
            .quando_vazio(preco, "O preço é um campo obrigatorio")\
            .quando_vazio(categoria, "A categoria é um campo obrigatorio")\
            .lancar()
