MENU = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3

#Funcao específica para depositar
def depositar(valor):
    global saldo, extrato
    if valor > 0:
        saldo += valor
        extrato.append(f"Depósito: R$ {valor:.2f}")
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")

#Funcao específica para sacar
def sacar(valor):
    global saldo, extrato, numero_saques
    if valor > 0 and valor <= limite and numero_saques < LIMITE_SAQUES: #limite de saques possíveis.
        if saldo >= valor:
            saldo -= valor
            extrato.append(f"Saque: R$ {valor:.2f}")
            numero_saques += 1
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Operação falhou! Você não tem saldo suficiente.")
    else:
        print("Operação falhou! Valor inválido para saque ou limite de saques diários atingido.")

def exibir_extrato():
    print("\n================ EXTRATO ================")
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        for movimentacao in extrato:
            print(movimentacao)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

while True:
    opcao = input(MENU)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        depositar(valor)

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        sacar(valor)

    elif opcao == "e":
        exibir_extrato()

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
