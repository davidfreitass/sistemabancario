from pessoas.pessoas import Pessoa
from cliente.cliente import Cliente
from conta.conta import Conta


class Menu:
    """
    Menu inicial do Sistema Bancário
    """
    lista_clientes: list = []
    lista_bancos: list = []
    lista_pessoas: list = []

    def menu(self):
        print("""
            Bem vindo(a) ao sistema. Escolha a opção desejada: 
                1 - Administrar o Sistema
                2 - Acessar como Cliente
                3 - Sair
        """)
        while True:
            escolha = int(input("Sua opção: "))
            if escolha not in range(1, 4):
                print("Escolha inválida. Tente novamente!")
            elif escolha == 1:
                self.menu_principal()
            elif escolha == 2:
                self.menu_cliente()
            elif escolha == 3:
                self.sair()

    def menu_principal(self):
        print("""
            ADMINISTRAÇÃO DO SISTEMA
                Escolha a opção desejada:
                    1 - Gerenciar Bancos
                    2 - Gerenciar Pessoas
                    3 - Gerenciar Agências
                    4 - Gerenciar Contas
                    5 - Voltar Menu Anterior
        """)
        while True:
            escolha = int(input("Sua opção: "))
            if escolha not in range(1, 6):
                print("Escolha inválida. Tente novamente!")
            else:
                if escolha == 1:
                    pass
                elif escolha == 2:
                    self.menu_pessoa()
                elif escolha == 3:
                    pass
                elif escolha == 4:
                    self.menu_contas()
                elif escolha == 5:
                    self.menu()
                else:
                    print("Escolha inválida. Tente novamente!")

    def exibir_menu_cliente(self, nome_pessoa):
        print(f"""
                    ACESSO DO CLIENTE
                            Cliente selecionado: {nome_pessoa}

                            Escolha a opção desejada:
                                1 - Listar minhas contas bancárias
                                2 - Efetuar Depósito
                                3 - Efetuar Saque
                                4 - Efetuar Transferência
                                5 - Obter Extrato
                                6 - Voltar Menu Anterior
                            """)

    def menu_cliente(self):
        for i, cliente in enumerate(self.lista_clientes):
            print(f"[{i}] {cliente.pessoa.nome}")
        while True:
            opcao = int(
                input(f"Deseja selecionar qual cliente? [999 para voltar] "))
            if opcao == 999:
                self.menu()
            elif opcao not in range(0, len(self.lista_clientes)):
                print("Escolha inválida. Tente novamente!")
            else:
                nome_pessoa = self.lista_clientes[opcao].pessoa.nome
                self.exibir_menu_cliente(nome_pessoa)
                while True:
                    escolha = int(input("Sua opção: "))
                    if escolha not in range(1, 7):
                        print("Escolha inválida. Tente novamente!")
                    else:
                        if escolha == 1:
                            for i, conta in enumerate(self.lista_clientes[opcao].contas):
                                bancos1 = f"[{i}] {conta.banco}"
                                print('='*len(bancos1))
                                print(bancos1)
                                print('='*len(bancos1))
                            self.exibir_menu_cliente(nome_pessoa)
                        elif escolha == 2:
                            for i, conta in enumerate(self.lista_clientes[opcao].contas):
                                print(f"[{i}] {conta.banco}")
                            while True:
                                conta_deposito = int(input("Em que conta? "))
                                if conta_deposito not in range(0, len(self.lista_clientes[opcao].contas)):
                                    print("Escolha inválida. Tente novamente!")
                                else:
                                    print(
                                        '='*len(f"Qual valor deseja depositar no banco {self.lista_clientes[opcao].contas[conta_deposito].banco}? "))
                                    valor_deposito = float(
                                        input(f"Qual valor deseja depositar no banco {self.lista_clientes[opcao].contas[conta_deposito].banco}? "))
                                    self.lista_clientes[opcao].contas[conta_deposito].deposito(
                                        valor_deposito)
                                    self.lista_clientes[opcao].contas[conta_deposito].extrato(
                                    )
                                    self.exibir_menu_cliente(nome_pessoa)
                                    break
                        elif escolha == 3:
                            for i, conta in enumerate(self.lista_clientes[opcao].contas):
                                bancos2 = f"[{i}] {conta.banco}"
                                print('='*len(bancos2))
                                print(bancos2)
                                print('='*len(bancos2))
                            while True:
                                conta_saque = int(
                                    input("Deseja sacar em que conta? "))
                                if conta_saque not in range(0, len(self.lista_clientes[opcao].contas)):
                                    print("Escolha inválida. Tente novamente!")
                                else:
                                    print(
                                        '='*len(f"Quanto deseja sacar no banco {self.lista_clientes[opcao].contas[conta_saque].banco}? "))
                                    valor_saque = float(
                                        input(f"Quanto deseja sacar no banco {self.lista_clientes[opcao].contas[conta_saque].banco}? "))
                                    self.lista_clientes[opcao].contas[conta_saque].saque(
                                        valor_saque)
                                    self.lista_clientes[opcao].contas[conta_saque].extrato(
                                    )
                                    self.exibir_menu_cliente(nome_pessoa)
                                    break
                        elif escolha == 4:
                            for i, conta in enumerate(self.lista_clientes[opcao].contas):
                                bancos3 = f"[{i}] {conta.banco}"
                                print('='*len(bancos3))
                                print(bancos3)
                                print('='*len(bancos3))
                            while True:
                                conta_transferencia_1 = int(
                                    input("De qual conta? "))
                                if conta_transferencia_1 not in range(0, len(self.lista_clientes[opcao].contas)):
                                    print(
                                        "Escolha inválida. Tente novamente!")
                                else:
                                    for i, cliente in enumerate(self.lista_clientes):
                                        if cliente.pessoa.nome == nome_pessoa:
                                            pass
                                        else:
                                            clientes = f"[{i}] {cliente.pessoa.nome}"
                                            print('='*len(clientes))
                                            print(clientes)
                                            print('='*len(clientes))
                                    while True:
                                        opcao_transferencia = int(
                                            input(f"Para qual cliente? [999 para voltar] "))
                                        if opcao_transferencia == 999:
                                            self.exibir_menu_cliente()
                                        elif opcao_transferencia not in range(0, len(self.lista_clientes)):
                                            print(
                                                "Escolha inválida. Tente novamente!")
                                        else:
                                            for i, conta in enumerate(self.lista_clientes[opcao_transferencia].contas):
                                                bancos4 = f"[{i}] {conta.banco}"
                                                print('='*len(bancos4))
                                                print(bancos4)
                                                print('='*len(bancos4))
                                            while True:
                                                conta_transferencia_2 = int(
                                                    input("Para qual conta? "))
                                                if conta_transferencia_2 not in range(0, len(self.lista_clientes[opcao_transferencia].contas)):
                                                    print(
                                                        "Escolha inválida. Tente novamente!")
                                                else:
                                                    print(
                                                        '='*len(f"Qual valor transferir para o cliente {self.lista_clientes[opcao_transferencia].pessoa.nome}? "))
                                                    valor_transferencia = float(input(
                                                        f"Qual valor transferir para o cliente {self.lista_clientes[opcao_transferencia].pessoa.nome}? "))
                                                    self.lista_clientes[opcao].contas[conta_transferencia_1].saque(
                                                        valor_transferencia)
                                                    self.lista_clientes[opcao_transferencia].contas[conta_transferencia_2].deposito(
                                                        valor_transferencia)
                                                    self.exibir_menu_cliente(
                                                        nome_pessoa)
                                                    break
                                            break
                                    break
                        elif escolha == 5:
                            for i, conta in enumerate(self.lista_clientes[opcao].contas):
                                print(f"[{i}] {conta.banco}")
                            while True:
                                conta_extrato = int(
                                    input("Deseja receber o extrato de qual conta? "))
                                if conta_extrato not in range(0, len(self.lista_clientes[opcao].contas)):
                                    print("Escolha inválida. Tente novamente!")
                                else:
                                    self.lista_clientes[opcao].contas[conta_extrato].extrato(
                                    )
                                    self.exibir_menu_cliente(nome_pessoa)
                                    break
                        elif escolha == 6:
                            self.menu_cliente()

    def exibir_menu_pessoa(self):
        print("""
            GERENCIAR PESSOAS
                Escolha a opção desejada:
                    1 - Nova Pessoa (Futuro Cliente)
                    2 - Listar Pessoas
                    3 - Pesquisar Pessoa
                    4 - Excluir Pessoa
                    5 - Atualizar Pessoa
                    6 - Voltar Menu Anterior
        """)

    def menu_pessoa(self):
        self.exibir_menu_pessoa()
        while True:
            escolha = int(input("Sua opção: "))
            if escolha not in range(1, 7):
                print("Escolha inválida. Tente novamente!")
            else:
                if escolha == 1:
                    nome_pessoa = str(
                        input("Informe o nome da pessoa: ").upper())
                    cpf_pessoa = str(
                        input("Informe o CPF da pessoa: "))
                    idade_pessoa = int(
                        input("Informe a idade da pessoa: "))
                    new_pessoa = Pessoa(
                        nome=nome_pessoa,
                        cpf=cpf_pessoa,
                        idade=idade_pessoa
                    )
                    self.lista_pessoas.append(new_pessoa)
                    new_cliente = Cliente(pessoa=new_pessoa)
                    self.lista_clientes.append(new_cliente)
                    self.exibir_menu_pessoa()
                elif escolha == 2:
                    for i, pessoa in enumerate(self.lista_pessoas):
                        print(f"[{i}] {pessoa.nome}")
                    self.exibir_menu_pessoa()
                elif escolha == 3:
                    pes_pessoa = input(
                        "Qual pessoa deseja pesquisar pelo nome? ").upper()
                    for i, pessoa in enumerate(self.lista_pessoas):
                        if pes_pessoa == pessoa.nome:
                            print(
                                f"A pessoa {pes_pessoa} se encontra na lista de pessoas do sistema.")
                            self.exibir_menu_pessoa()
                            break
                        elif i == (len(self.lista_pessoas) - 1):
                            if (pes_pessoa == pessoa.nome) == False:
                                print(
                                    f"A pessoa {pes_pessoa} NÃO se encontra na lista de pessoas do sistema.")
                                self.exibir_menu_pessoa()
                        else:
                            continue
                # elif escolha == 4:
                #     print("-" * 30)
                #     for i, p in enumerate(self.lista_pessoas):
                #         print(f"[{i}]: {p.nome}")
                #     print("-" * 30)
                #     excluir_pessoa = int(
                #         input("Deseja excluir qual pessoa? "))
                #     print(
                #         f"A pessoa {} foi removida com sucesso!")
                #     print("Nova lista de pessoas: ")
                #     for i, p in enumerate(self.lista_pessoas):
                #         print(f"[{i}]: {p.nome}")
                # elif escolha == 5:
                #     print("-" * 30)
                #     for i, b in enumerate(pessoas):
                #         print(f"[{i}]: {b}")
                #     print("-" * 30)
                #     atualizar_pessoa = int(
                #         input("Deseja atualizar qual pessoa? "))
                #     pessoas[atualizar_pessoa] = input(
                #         f"Atualizar pessoa {pessoas[atualizar_pessoa]} para: ").upper()
                #     print(
                #         f"A pessoa {pessoas[atualizar_pessoa]} foi atualizada com sucesso!")
                #     print(f"Nova lista de pessoas: {pessoas}")
                elif escolha == 6:
                    self.menu_principal()

    def exibir_menu_contas(self, nome_pessoa):
        print(f"""
                            Cliente selecionado: {nome_pessoa}

                            Escolha a opção desejada:
                                1 - Adicionar Conta
                                2 - Excluir Conta
                                3 - Voltar Menu Anterior
                            """)

    def menu_contas(self):
        for i, cliente in enumerate(self.lista_clientes):
            print(f"[{i}] {cliente.pessoa.nome}")
        while True:
            opcao = int(
                input(f"Deseja selecionar qual cliente? [999 para voltar] "))
            if opcao == 999:
                self.menu_principal()
            elif opcao not in range(0, len(self.lista_clientes)):
                print("Escolha inválida. Tente novamente!")
            else:
                nome_pessoa = self.lista_clientes[opcao].pessoa.nome
                self.exibir_menu_contas(nome_pessoa)
                while True:
                    escolha = int(input("Sua opção: "))
                    if escolha not in range(1, 4):
                        print("Escolha inválida. Tente novamente!")
                    else:
                        if escolha == 1:
                            banco = str(input("Nome do banco: ").upper())
                            nova_conta = Conta(banco=banco)
                            self.lista_clientes[opcao].vincular_conta(
                                nova_conta)
                            frase = f"Foi adicionado uma conta no banco {banco} a pessoa {nome_pessoa}."
                            print('=' * len(frase))
                            print(frase)
                            print('=' * len(frase))
                            self.exibir_menu_contas(nome_pessoa)
                        elif escolha == 2:
                            pass
                        elif escolha == 3:
                            self.menu_contas()

    def sair(self):
        print("Saindo do programa...")
        exit()
