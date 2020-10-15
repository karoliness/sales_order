from domain.domain_exception import DomainException


class Categoria:
    def __init__(self, nome: str):
        self.validar(nome)
        self.nome = nome

    def validar(self, nome):
        DomainException().quando_vazio(nome, "O campo nome é um campo obrigatório").lancar()
