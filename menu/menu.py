from pessoas.pessoas import Pessoa
from cliente.cliente import Cliente


class Menu:
    """
    Menu inicial do Sistema Bancário
    """
    lista_clientes: list = []
    lista_bancos: list = []
    lista_pessoas: list = []
    lista_temporaria: list = []

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
            else:
                print("Escolha inválida. Tente novamente!")

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
                    pass
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
        opcao = int(
            input(f"Deseja selecionar qual cliente? [999 para voltar] "))
        if opcao == 999:
            self.menu()
        nome_pessoa = self.lista_clientes[opcao].pessoa.nome
        self.exibir_menu_cliente(nome_pessoa)
        while True:
            escolha = int(input("Sua opção: "))
            if escolha not in range(1, 7):
                print("Escolha inválida. Tente novamente!")
            else:
                if escolha == 1:
                    pass
                elif escolha == 2:
                    valor_deposito = float(
                        input("Qual valor deseja depositar? "))
                    self.lista_clientes[opcao].deposito(valor_deposito)
                    print(self.lista_clientes[opcao].extrato())
                    self.exibir_menu_cliente(nome_pessoa)
                elif escolha == 3:
                    valor_saque = float(
                        input("Quanto deseja sacar? "))
                    self.lista_clientes[opcao].saque(valor_saque)
                    print(self.lista_clientes[opcao].extrato())
                    self.exibir_menu_cliente(nome_pessoa)
                elif escolha == 4:
                    pass
                elif escolha == 5:
                    print(self.lista_clientes[opcao].extrato())
                    self.exibir_menu_cliente(nome_pessoa)
                elif escolha == 6:
                    self.menu_cliente()
                else:
                    print("Escolha inválida. Tente novamente!")

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
                    cpf_pessoa = str(input("Informe o CPF da pessoa: "))
                    idade_pessoa = int(input("Informe a idade da pessoa: "))
                    new_pessoa = Pessoa(
                        nome=nome_pessoa,
                        cpf=cpf_pessoa,
                        idade=idade_pessoa
                    )
                    self.lista_pessoas.append(new_pessoa)
                    self.lista_clientes.append(Cliente(pessoa=new_pessoa))
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
                else:
                    print("Escolha inválida. Tente novamente!")

    def sair(self):
        print("Saindo do programa...")
        exit()
