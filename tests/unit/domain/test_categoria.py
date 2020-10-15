from unittest import TestCase
from domain.categoria import Categoria


class TestCategoria(TestCase):
    def test_deve_criar_uma_categoria_valida(self):
        nome = "Informática"
        resposta_esperada = {
            "nome": nome
        }

        resposta_encontrada = Categoria(nome)

        self.assertDictEqual(resposta_esperada, resposta_encontrada.__dict__)

    def test_deve_validar_categoria_quando_nao_possui_nome(self):
        erro_esperado = "O campo nome é um campo obrigatório"
        nome = ""

        with self.assertRaises(Exception) as context:
            Categoria(nome)

        self.assertEqual(erro_esperado, context.exception.args[0][0])

    def test_deve_validar_categoria_quando_possui_nome(self):
        nome_esperado = "Karol"

        categoria = Categoria(nome_esperado)

        self.assertEqual(nome_esperado, categoria.nome)
