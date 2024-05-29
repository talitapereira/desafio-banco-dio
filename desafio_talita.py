menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

Escolha uma opção: """

saldo = 0.0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

opcao = ""
while opcao != "q":
    print(menu)
    opcao = input("")

    if opcao == "d":
        deposito = float(input("Digite o valos a ser depositado: "))
        # impede depósitos menor ou igual a zero
        if deposito <= 0:
            print("Valor de depósito inválido.")
            continue
        else:
            saldo += deposito
            extrato += f"Depósito: R$ {deposito:.2f}\n"
            print(f"Novo saldo: R$ {saldo:.2f}")
    
    
    if opcao == "s":
        saque = float(input("Digite o valor a ser sacado:"))
        # impede número de saques maior que o limite de saque estabelecido
        if numero_saques >= LIMITE_SAQUES:
            print("Número de saques diários excedido.")
            continue

        if saque > limite:
            print(f"Limite de saque excedido. Saque máximo R$ {limite:.2f}")
            continue

        if saque > saldo:
            print("Você não tem saldo suficiente.")
            continue

        if saque <= 0:
            print("Valor de saque inválido.")
            continue

        else:
            # exibe os saques e depósitos realizados
            saldo -= saque
            extrato += f"Saque: R$ {saque:.2f}\n"
            numero_saques += 1
            print(f"Novo saldo: R$ {saldo:.2f}")


    
    if opcao == "e":
        print("Extrato:\n ")
        print(extrato)
        print(f"Saldo: R$ {saldo:.2f}")
