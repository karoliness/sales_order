from unittest import TestCase
from domain.endereco import Endereco


class TestEndereco(TestCase):
    def test_deve_validar_quando_nao_possui_rua(self):
        rua = ""
        erro_esperado = "A rua é um campo obrigatório"

        with self.assertRaises(Exception) as context:
            Endereco(rua, "10", "Vila Cruzeiro",
                     "São Paulo", "SP", "53454353")

        self.assertTrue(erro_esperado in context.exception.args[0])

    def test_deve_validar_quando_nao_possui_numero(self):
        numero = ""
        erro_esperado = "O numero é um campo obrigatório"

        with self.assertRaises(Exception) as context:
            Endereco("Luis correia", numero, "Vila Cruzeiro",
                     "São Paulo", "SP", "53454353")

        self.assertTrue(erro_esperado in context.exception.args[0])

    def test_deve_validar_quando_nao_possui_bairro(self):
        bairro = ""
        erro_esperado = "O bairro é um campo obrigatório"

        with self.assertRaises(Exception) as context:
            Endereco("Luis correia", "10", bairro,
                     "São Paulo", "SP", "53454353")

        self.assertTrue(erro_esperado in context.exception.args[0])

    def test_deve_validar_quando_nao_possui_cidade(self):
        cidade = ""
        erro_esperado = "A cidade é um campo obrigatório"

        with self.assertRaises(Exception) as context:
            Endereco("Luis correia", "10", "Vila Cruzeiro",
                     cidade, "SP", "53454353")

        self.assertTrue(erro_esperado in context.exception.args[0])

    def test_deve_validar_quando_nao_possui_estado(self):
        estado = ""
        erro_esperado = "O estado é um campo obrigatório"

        with self.assertRaises(Exception) as context:
            Endereco("Luis correia", "10", "Vila Cruzeiro",
                     "São Paulo", estado, "53454353")

        self.assertTrue(erro_esperado in context.exception.args[0])

    def test_deve_validar_quando_nao_possui_cep(self):
        cep = ""
        erro_esperado = "O cep é um campo obrigatório"

        with self.assertRaises(Exception) as context:
            Endereco("Luis correia", "10", "Vila Cruzeiro",
                     "São Paulo", "SP", cep)

        self.assertTrue(erro_esperado in context.exception.args[0])

    def test_deve_criar_um_endereco_valido(self):
        endereco = {
            "rua": "Rua Luis Correia",
            "numero": "10",
            "bairro": "Vila Cruzeiro",
            "cidade": "Sao Paulo",
            "estado": "SP",
            "cep": "3654645",
            "complemento": ""
        }

        endereco_encontrado = Endereco(**endereco)

        self.assertDictEqual(endereco, endereco_encontrado.__dict__)
