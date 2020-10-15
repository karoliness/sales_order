from unittest import TestCase
from domain.domain_exception import DomainException


class TestDomainException(TestCase):
    def test_deve_validar_quando_um_valor_eh_vazio(self):
        valor = None
        mensagem_de_erro_esperado = "O valor é um campo obrigatorio"

        erro_encontrado = DomainException().quando_vazio(
            valor, mensagem_de_erro_esperado)

        self.assertEqual(mensagem_de_erro_esperado,
                         erro_encontrado.mensagens[0])

    def test_deve_validar_quando_um_valor_nao_eh_vazio(self):
        valor = "Qualquer coisa"
        mensagem = "A qualquer coisa é obrigatorio"
        resposta_esperada = []

        resposta_encontrada = DomainException().quando_vazio(valor, mensagem)

        self.assertEqual(resposta_esperada, resposta_encontrada.mensagens)

    def test_deve_lancar_a_excessao(self):
        rua = None
        numero = None
        erro_esperado = ("A rua é um campo obrigatório",
                         "O numero é um campo obrigatório")

        with self.assertRaises(Exception) as context:
            DomainException()\
                .quando_vazio(rua, "A rua é um campo obrigatório")\
                .quando_vazio(numero, "O numero é um campo obrigatório")\
                .lancar()

        self.assertCountEqual(erro_esperado, context.exception.args[0])
