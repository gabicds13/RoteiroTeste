from Model.conta import Conta
from Model.Cliente import Cliente
from Model.Deposito import Deposito
from Model.pessoa import Pessoa
from datetime import date


def teste_unitario_deposito():
    # --- TESTE 1: DEPÓSITO ---
    print("--- Executando Teste 1: Depósito ---")
    cliente = Cliente("João", "123", "Rua A")
    conta = Conta(101, cliente)
    deposito = Deposito(200.0)
    deposito.registrar(conta)

    if conta.saldo == 200.0:
        print("✅ Teste 1 (Depósito) PASSOU!")
    else:
        print("❌ Teste 1 FALHOU!")


def teste_unitario_nome_ausente():
    # --- TESTE 2: NOME AUSENTE ---
    print("\n--- Iniciando Teste 2: Validação de Nome Ausente ---")
    endereco = "Rua Insper, 409"
    nascimento = date(2000, 1, 1)
    cpf = "111.222.333-44"
    nome_vazio = ""

    # Importante: O erro de super().__init__ precisa estar corrigido em pessoa.py
    novo_cliente = Pessoa(endereco, nascimento, cpf, nome_vazio)

    if novo_cliente._nome == "":
        print("❌ Teste 2 FALHOU: O sistema permitiu criar um cliente sem nome!")
        print("   (Justificativa: Falta validação de integridade na classe Pessoa)")
    else:
        print("✅ Teste 2 PASSOU: O sistema bloqueou o nome vazio.")


if __name__ == "__main__":
    teste_unitario_deposito()
    teste_unitario_nome_ausente()