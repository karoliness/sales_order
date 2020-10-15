from unittest import TestCase
from domain.cpf import Cpf


class TestCpf(TestCase):
    def test_deve_validar_cpf_sem_mascara_quando_cpf_eh_valido(self):
        cpf_esperado = "03834163104"

        cpf_encontrado = Cpf(cpf_esperado)

        self.assertEqual(cpf_esperado, cpf_encontrado.valor)

    def test_deve_validar_cpf_com_mascara_quando_cpf_eh_valido(self):
        cpf_esperado = "038.341.631-04"

        cpf_encontrado = Cpf(cpf_esperado)

        self.assertEqual(cpf_esperado, cpf_encontrado.valor)

    def test_deve_validar_cpf_sem_mascara_quando_cpf_eh_invalido(self):
        cpf = "038341631"
        erro_esperado = f'Esse {cpf} não é válido'

        with self.assertRaises(Exception) as context:
            Cpf(cpf)

        self.assertTrue(erro_esperado in context.exception.args)

    def test_deve_validar_cpf_com_mascara_quando_cpf_eh_invalido(self):
        cpf = "038.341.631"
        erro_esperado = f'Esse {cpf} não é válido'

        with self.assertRaises(Exception) as context:
            Cpf(cpf)

        self.assertTrue(erro_esperado in context.exception.args)
