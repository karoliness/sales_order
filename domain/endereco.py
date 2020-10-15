from domain.domain_exception import DomainException


class Endereco:
    def __init__(self, rua: str, numero: str, bairro: str, cidade: str, estado: str, cep: str, complemento: str = ""):
        self.validar(rua, numero, complemento, bairro, cidade, estado, cep)
        self.rua = rua
        self.numero = numero
        self.complemento = complemento
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado
        self.cep = cep

    def validar(self, rua, numero, complemento, bairro, cidade, estado, cep):
        DomainException()\
            .quando_vazio(rua, "A rua é um campo obrigatório")\
            .quando_vazio(numero, "O numero é um campo obrigatório")\
            .quando_vazio(bairro, "O bairro é um campo obrigatório")\
            .quando_vazio(cidade, "A cidade é um campo obrigatório")\
            .quando_vazio(estado, "O estado é um campo obrigatório")\
            .quando_vazio(cep, "O cep é um campo obrigatório")\
            .lancar()
