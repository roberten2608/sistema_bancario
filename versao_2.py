"""
Módulo responsável pelo sistema bancário.
Este script implementa uma solução para gerenciar depósitos, saques e saldos.
"""
from datetime import datetime

# Classe para gerenciar informações de usuários
class Usuario:
    def __init__(self, nome, cpf, data_nascimento, endereco):
        self.nome = nome               # Nome do usuário
        self.cpf = cpf                 # CPF do usuário
        self.data_nascimento = data_nascimento  # Data de nascimento do usuário
        self.endereco = endereco       # Endereço do usuário

# Classe para gerenciar operações bancárias de uma conta
class Conta:
    def __init__(self, usuario):
        self.usuario = usuario         # Associar conta a um usuário
        self.saldo = 0.0               # Saldo inicial da conta
        self.depositos = []            # Lista de depósitos
        self.saques = []               # Lista de saques
        self.transacoes_diarias = 0    # Contador de transações diárias
        self.saques_diarios = 0        # Contador de saques diários

    # Validar se uma transação pode ser realizada
    def validar_transacao(self, tipo):
        if tipo == 'geral' and self.transacoes_diarias >= MAX_TRANSACOES_DIARIAS:
            print("Você excedeu o número de transações permitidas para hoje.")
            return False  # Transação geral excede limite
        elif tipo == 'saque' and self.saques_diarios >= MAX_SAQUES_DIARIOS:
            print("Limite diário de saques atingido!")
            return False  # Saque excede limite
        return True  # Transação permitida

    # Registrar uma transação na conta
    def registrar_transacao(self, tipo, valor):
        data_hora = datetime.now().strftime("%d-%m-%Y %H:%M:%S")  # Data e hora atuais
        if tipo == 'deposito':
            self.depositos.append((valor, data_hora))  # Adicionar depósito
        elif tipo == 'saque':
            self.saques.append((valor, data_hora))     # Adicionar saque
            self.saques_diarios += 1                   # Incrementar saques diários
        self.transacoes_diarias += 1                   # Incrementar transações diárias

# Constantes do sistema
MAX_TRANSACOES_DIARIAS = 10    # Limite de transações diárias
MAX_SAQUES_DIARIOS = 3         # Limite de saques diários
LIMITE_SAQUE = 500.00          # Limite de saque por transação

# Listas para armazenar usuários e contas
usuarios = []
contas = []

# Função para criar um novo usuário
def criar_usuario():
    nome = input("Digite seu nome: ")                 # Entrada de nome
    cpf = input("Digite seu CPF: ")                   # Entrada de CPF
    data_nascimento = input("Digite sua data de nascimento (DD/MM/AAAA): ")
    endereco = input("Digite seu endereço: ")         # Entrada de endereço

    if any(u.cpf == cpf for u in usuarios):           # Verifica duplicidade de CPF
        print("Usuário com este CPF já existe.")
        return None                                   # Retorna se CPF já existe

    # Cria novo usuário e adiciona à lista
    usuario = Usuario(nome, cpf, data_nascimento, endereco)
    usuarios.append(usuario)
    print("Usuário criado com sucesso!")
    return usuario                                    # Retorna usuário criado

# Função para criar uma nova conta associada a um usuário
def criar_conta(usuario):
    if any(c.usuario.cpf == usuario.cpf for c in contas):
        print("Este usuário já possui uma conta.")
        return None                                   # Verifica se o usuário já tem uma conta

    conta = Conta(usuario)                            # Cria nova conta
    contas.append(conta)                              # Adiciona conta à lista
    print("Conta criada com sucesso!")
    return conta                                      # Retorna conta criada

# Função para gerar relatório de contas
def criar_relatorio(contas):
    print("\n=== Relatório de Contas ===")
    for conta in contas:
        # Exibe detalhes de cada conta
        print(f"Usuário: {conta.usuario.nome}, CPF: {conta.usuario.cpf}, Saldo: R$ {conta.saldo:.2f}")

# Função principal que controla o sistema
def main():
    while True:
        # Exibe menu de opções
        print("\n=== Banking System...versão 1.0 ===")
        print("1. Criar Usuário")
        print("2. Criar Conta")
        print("3. Depositar")
        print("4. Sacar")
        print("5. Extrato")
        print("6. Relatório de Contas")
        print("7. Sair")
        opcao = input("Escolha uma operação: ")  # Entrada da opção

        if opcao == "1":
            criar_usuario()  # Chama função para criar usuário

        elif opcao == "2":
            if not usuarios:
                print("Nenhum usuário encontrado. Crie um usuário primeiro.")
                continue  # Pede criação de usuário se não houver
            for i, usuario in enumerate(usuarios, start=1):
                print(f"{i}. {usuario.nome}, CPF: {usuario.cpf}")  # Lista usuários
            escolha = int(input("Escolha um usuário para associar à conta: ")) - 1
            if escolha < 0 or escolha >= len(usuarios):
                print("Usuário inválido. Por favor, selecione um usuário existente.")
                continue  # Valida escolha de usuário
            usuario = usuarios[escolha]  # Seleciona usuário
            criar_conta(usuario)  # Cria conta para usuário

        elif opcao in ["3", "4", "5"]:
            if not contas:
                print("Nenhuma conta encontrada. Crie uma conta primeiro.")
                continue  # Pede criação de conta se não houver
            for i, conta in enumerate(contas, start=1):
                print(f"{i}. {conta.usuario.nome}, CPF: {conta.usuario.cpf}")  # Lista contas
            escolha = int(input("Escolha uma conta: ")) - 1
            if escolha < 0 or escolha >= len(contas):
                print("Conta inválida. Por favor, selecione uma conta existente.")
                continue  # Valida escolha de conta
            conta = contas[escolha]  # Seleciona conta

            if opcao == "3":  # Depositar
                if not conta.validar_transacao('geral'):
                    continue  # Valida transação
                valor_input = input("Digite o valor do depósito: R$ ")
                try:
                    valor = float(valor_input)  # Converte entrada para float
                except ValueError:
                    print("Valor inválido! Por favor, digite um número.")
                    continue  # Lida com erro de conversão

                if valor > 0:
                    conta.saldo += valor  # Atualiza saldo
                    conta.registrar_transacao('deposito', valor)  # Registra depósito
                    print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
                else:
                    print("O valor do depósito deve ser positivo.")

            elif opcao == "4":  # Sacar
                if not conta.validar_transacao('saque'):
                    continue  # Valida transação
                valor_input = input("Digite o valor do saque: R$ ")
                try:
                    valor = float(valor_input)  # Converte entrada para float
                except ValueError:
                    print("Valor inválido! Por favor, digite um número.")
                    continue  # Lida com erro de conversão

                if valor <= 0:
                    print("O valor do saque deve ser positivo.")
                elif valor > LIMITE_SAQUE:
                    print(f"Não é permitido sacar mais do que R$ {LIMITE_SAQUE:.2f} por operação.")
                elif valor > conta.saldo:
                    print("Saldo insuficiente para essa operação.")
                else:
                    conta.saldo -= valor  # Atualiza saldo
                    conta.registrar_transacao('saque', valor)  # Registra saque
                    print(f"Saque de R$ {valor:.2f} realizado com sucesso!")

            else:  # Extrato
                print("\n=== Extrato ===")
                if not conta.depositos and not conta.saques:
                    print("Não foram realizadas movimentações.")
                else:
                    if conta.depositos:
                        print("Depósitos:")
                        for valor, data_hora in conta.depositos:
                            print(f"R$ {valor:.2f} em {data_hora}")  # Exibe depósitos
                    if conta.saques:
                        print("Saques:")
                        for valor, data_hora in conta.saques:
                            print(f"R$ {valor:.2f} em {data_hora}")  # Exibe saques
                    print(f"\nSaldo atual: R$ {conta.saldo:.2f}")

        elif opcao == "6":
            criar_relatorio(contas)  # Chama função para criar relatório

        elif opcao == "7":
            print("Encerrando o sistema. Obrigado por usar nossos serviços!")
            break  # Termina o programa

        else:
            print("Opção inválida! Por favor, escolha uma operação válida.")

# Executa a função principal
if __name__ == "__main__":
    main()
