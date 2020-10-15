class DomainException:
    def __init__(self):
        self.mensagens = []

    def quando_vazio(self, valor, mensagem):
        if not valor:
            self.mensagens.append(mensagem)
        return self

    def lancar(self):
        if self.mensagens:
            raise Exception(self.mensagens)
