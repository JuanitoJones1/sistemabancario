""" sistema bancário com três operações: depósito, saque e extrato

Depósito: deve ser possível depositar apenas valores positivos
Todos os depósitos devem ser armazenados em uma variável e exibido no extrato

Saque: o sistema deve permitir 3 saques diários com limite máximo de $500
Caso o usuário não tenha saldo em conta, o sistema deve exibir informando falta de saldo
Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato


Extrato: deve listar todo os depósitos e saques realizados
No fim, deve ser exibido o saldo atual da conta
Deve ser exibido com o formato R$---.--

"""
menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação inválida! Saldo insuficiente.")

        elif excedeu_limite:
            print("Operação inválida! Valor de saque excedido.")

        elif excedeu_saques:
            print("Operação inválida! Número de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação inválida! O valor informado é inválido.")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")