
from Model.Historico import Historico
class Conta:
    def __init__ (self,numero: int, cliente: 'Cliente'):
        #numero e cliente sao informacoes  que serao entradas
        self._saldo = 0.0
        #._ significa privado
        self._cliente = cliente
        self._agencia = "0001"
        self._numero = numero
        self._historico = Historico()

    @property #->property para poder acessar o saldo de forma segura
    def saldo(self) -> float:
        return self._saldo

    @classmethod
    def nova_conta(cls, cliente: 'Cliente', numero: int):
        return cls(numero, cliente)

    def sacar(self, valor: float) -> bool:
        if valor > 0 and self._saldo >= valor:
            self._saldo -= valor
            return True  # Saque com sucesso
        return False


    def depositar(self, valor: float) -> bool:
            if valor > 0:
                self._saldo += valor
                return True  # Depósito com sucesso
            return False



