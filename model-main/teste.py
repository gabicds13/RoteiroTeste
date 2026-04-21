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


def teste_integracao_fluxo_deposito_historico():
    print("\n--- Executando Teste de Integração: Fluxo Depósito -> Histórico ---")

    cliente = Cliente("Gabi", "444.555.666-77", "Rua do Insper, 123")
    conta = Conta(numero=202, cliente=cliente)
    valor = 150.0
    deposito = Deposito(valor)


    deposito.registrar(conta)

    saldo_correto = conta.saldo == 150.0
    historico_preenchido = len(conta._historico.transacoes) > 0

    if saldo_correto and historico_preenchido:
        print("✅ Teste de Integração PASSOU!")
        print(f"   Saldo atualizado: {conta.saldo}")
        print(f"   Transações no histórico: {len(conta._historico.transacoes)}")
    else:
        print("❌ Teste de Integração FALHOU!")
        if not historico_preenchido:
            print("   Erro: A transação não foi salva no histórico.")


if __name__ == "__main__":
    teste_unitario_deposito()
    teste_unitario_nome_ausente()
    teste_integracao_fluxo_deposito_historico()


    #teste de integração


