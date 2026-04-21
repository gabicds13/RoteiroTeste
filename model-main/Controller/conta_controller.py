from Model.BancoDeDados import BancoDados
from Model.Cliente import Cliente
from Model.Conta_corrente import ContaCorrente


class ContaController:

    def __init__(self, view):
        self.view = view
        self.banco = BancoDados()
        self.numero_conta = 1


    def criar_conta(self):

        nome, cpf, endereco = self.view.obter_dados()

        # cria cliente
        cliente = Cliente(nome, cpf, endereco)

        # cria conta
        conta = ContaCorrente(self.numero_conta, cliente, 500, 3)

        self.numero_conta += 1

        # salva no banco
        self.banco.salvar_conta(conta)

        # mostra resultado
        texto = f"""
Conta criada com sucesso!

Cliente: {cliente.nome}
CPF: {cliente.cpf}
Número da conta: {conta._numero}
Agência: {conta._agencia}
Saldo: R$ {conta.saldo:.2f}
"""

        self.view.mostrar_conta(texto)
        self.view.limpar_campos()