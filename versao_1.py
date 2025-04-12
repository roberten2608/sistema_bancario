"""
Módulo responsável pelo sistema bancário.
Este script implementa uma solução para gerenciar depósitos, saques e saldos.
"""
# Sistema Bancário Simples: Depósito, Saque e Extrato

# variáveis
saldo = 0.0             # Saldo atual da conta
depositos = []          # Lista para armazenar os depósitos realizados
saques = []             # Lista para armazenar os saques realizados
saques_disponiveis = 3   # Número máximo de saques diários permitidos
LIMITE_SAQUE = 500.00  # Valor máximo permitido por saque

while True:
    # Exibição do menu para o usuário
    print("\n=== Banking System...versão 1.0 ===")
    print("== Escolha uma opção ==")
    print("1. Depositar")
    print("2. Sacar")
    print("3. Extrato")
    print("4. Sair")
    opcao = input("Escolha uma operação: ")

    if opcao == "1":
        # Operação de Depósito
        valor_input = input("Digite o valor do depósito: R$ ")
        try:
            valor = float(valor_input)  # Converte a entrada para número flutuante
        except ValueError:
            print("Valor inválido! Por favor, digite um número.")
            continue  # Pula para a próxima iteração do loop

        if valor > 0:
            saldo += valor         # Atualiza o saldo com o valor depositado
            depositos.append(valor)   # Armazena o valor do depósito
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("O valor do depósito deve ser positivo.")

    elif opcao == "2":
        # Operação de Saque

        # Verifica se ainda há saques disponíveis no dia
        if saques_disponiveis == 0:
            print("Limite diário de saques atingido!")
            continue

        valor_input = input("Digite o valor do saque: R$ ")
        try:
            valor = float(valor_input)  # Tenta converter a entrada para float
        except ValueError:
            print("Valor inválido! Por favor, digite um número.")
            continue

        # Valida se o valor digitado atende os requisitos do saque
        if valor <= 0:
            print("O valor do saque deve ser positivo.")
        elif valor > LIMITE_SAQUE:
            print(f"Não é permitido sacar mais do que R$ {LIMITE_SAQUE:.2f} por operação.")
        elif valor > saldo:
            print("Saldo insuficiente para essa operação.")
        else:
            saldo -= valor         # Atualiza o saldo diminuindo o valor sacado
            saques.append(valor)   # Armazena o valor do saque
            saques_disponiveis -= 1 # Diminui a quantidade de saques permitidos no dia
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!")

    elif opcao == "3":
        # Operação de Extrato
        print("\n=== Extrato ===")
        if not depositos and not saques:
            print("Não foram realizadas movimentações.")
        else:
            # Exibe os depósitos realizados, se houver
            if depositos:
                print("Depósitos:")
                for indice, dep in enumerate(depositos, start=1):
                    print(f"{indice}. R$ {dep:.2f}")
            # Exibe os saques realizados, se houver
            if saques:
                print("Saques:")
                for indice, sac in enumerate(saques, start=1):
                    print(f"{indice}. R$ {sac:.2f}")
            # Mostra o saldo atual da conta
            print(f"\nSaldo atual: R$ {saldo:.2f}")

    elif opcao == "4":
        # Encerramento do programa
        print("Encerrando o sistema. Obrigado por usar nossos serviços!")
        break  # Sai do loop e termina a execução do programa

    else:
        # Opção inválida escolhida pelo usuário
        print("Opção inválida! Por favor, escolha uma operação válida.")
