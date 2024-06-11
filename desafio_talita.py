def depositar(saldo, extrato, /):
    deposito = float(input("Digite o valor a ser depositado: "))
    # impede depósitos menor ou igual a zero
    if deposito <= 0:
        print("Valor de depósito inválido.")
    else:
        saldo += deposito
        extrato += f"Depósito: R$ {deposito:.2f}\n"
        print(f"Novo saldo: R$ {saldo:.2f}")
    
    return saldo, extrato
        
def sacar(*, numero_saques, saldo, extrato):
    saque = float(input("Digite o valor a ser sacado:"))
    # impede número de saques maior que o limite de saque estabelecido
    if numero_saques >= LIMITE_SAQUES:
        print("Número de saques diários excedido.")
    elif saque > LIMITE:
        print(f"Limite de saque excedido. Saque máximo R$ {LIMITE:.2f}")
    elif saque > saldo:
        print("Você não tem saldo suficiente.")
    elif saque <= 0:
        print("Valor de saque inválido.")
    else:
        # exibe os saques e depósitos realizados
        saldo -= saque
        extrato += f"Saque: R$ {saque:.2f}\n"
        numero_saques += 1
        print(f"Novo saldo: R$ {saldo:.2f}")
        
    return numero_saques, saldo, extrato

def visualizar_extrato(extrato, /, *, saldo):
    print("Extrato:\n ")
    print(extrato)
    print(f"Saldo: R$ {saldo:.2f}")
    
def cadastrar_cliente(dicionario: dict):
    cliente = dict()
    
    print("\nCadastre o cliente:\n")
    
    cliente["nome"] = input("Digite o nome completo: ")
    cliente["data_nascimento"] = input("Digite sua data de nascimento: ") 
    cliente["cpf"] = input("Digite o seu CPF: ")
    cliente["endereco"] = input("Digite seu endereço: ")
    
    cpf_cliente = cliente["cpf"] 

    if cpf_cliente in dicionario:
        print("\n Este cliente já existe!")
    else:
        dicionario[cpf_cliente] = cliente
        print(f"Cliente cadastrado com sucesso!\n")
    
    return dicionario

def cadastrar_conta(dicionario: dict, numero_conta):
    conta = dict()
    conta["agencia"] = AGENCIA
    conta["numero"] = numero_conta
    conta["cpf"] = input("Digite o seu CPF: ")
    
    cpf_cliente = conta["cpf"] 
    
    if cpf_cliente in dicionario:
        numero_conta += 1
        lista_contas.append(conta)
        print("Conta cadastrada com sucesso.\n")
    else:
        print("Conta não cadastrada : o cliente não existe")                                                                                                                                                                                                                                                                                  
    


menu = """

[c]  Cadastrar cliente
[cc] Cadastrar conta corrente
[d]  Depositar
[s]  Sacar
[e]  Extrato
[q]  Sair

Escolha uma opção: """

saldo = 0.0
LIMITE = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
dicionario_clientes = dict()
lista_contas = []
AGENCIA = "0001"
numero_conta = 1

opcao = ""


while opcao != "q":
    print(menu)
    opcao = input("")

    if opcao == "d":
        saldo, extrato = depositar(saldo, extrato)
        
    elif opcao == "c":
        dicionario_clientes = cadastrar_cliente(dicionario_clientes)
        
        
    elif opcao == "s":
        numero_saques, saldo, extrato = sacar(numero_saques = numero_saques, saldo = saldo, extrato = extrato)
    
    elif opcao == "cc":
        cadastrar_conta(dicionario_clientes, numero_conta)
    
    if opcao == "e":
        visualizar_extrato(extrato, saldo = saldo)
