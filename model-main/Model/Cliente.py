class Cliente:

    def __init__(self, nome, cpf, endereco):
        self.nome = nome
        self.cpf = cpf
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        # O print tem que ficar "dentro" (com espaço) do def
        print("Realizando transação...")

    # Esse def tem que estar alinhado com o def de cima!
    def adicionar_conta(self, conta):
        self._contas.append(conta)
        print("Nova conta adicionada à lista do cliente!")