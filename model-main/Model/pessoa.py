from datetime import date
from Model.Cliente import Cliente


class Pessoa(Cliente):
    def __init__(self, endereco: str, data_nascimento: date, cpf: str, nome: str):
        # O super().__init__ deve enviar os dados na ordem que Cliente espera: nome, cpf, endereco
        super().__init__(nome, cpf, endereco)

        # Atributos específicos da classe Pessoa
        self._cpf = cpf
        self._nome = nome
        self._data_nascimento = data_nascimento