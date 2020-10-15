import re


class Cpf:
    def __init__(self, valor: str):
        self.validar(valor)
        self.valor = valor

    def validar(self, valor_cpf):
        valido = False
        cpf = ''.join(re.findall('\\d', str(valor_cpf)))

        if (not cpf) or (len(cpf) < 11):
            valido = False

        inteiros = list(map(int, cpf))
        novo = inteiros[:9]

        while len(novo) < 11:
            r = sum([(len(novo)+1-i)*v for i, v in enumerate(novo)]) % 11

            if r > 1:
                f = 11 - r
            else:
                f = 0
            novo.append(f)

        if novo == inteiros:
            valido = True
        if not valido:
            raise Exception(f'Esse {valor_cpf} não é válido')
