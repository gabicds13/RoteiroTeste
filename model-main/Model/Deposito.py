
class Deposito:  # Herda da Transacao


    def __init__(self, valor: float):
       self._valor = valor

    def registrar(self, conta):

       deu_certo = conta.depositar(self._valor)
       if deu_certo:
        conta._historico.adicionar_transacao(self)