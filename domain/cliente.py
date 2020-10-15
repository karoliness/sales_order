from domain.endereco import Endereco
from domain.cpf import Cpf


class Cliente:
    def __init__(self, nome: str, cpf: Cpf, endereco: Endereco):
        self.nome = nome
        self.cpf = cpf
        self.endereco = endereco
