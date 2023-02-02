from pessoas.pessoas import Pessoa
from cliente.cliente import Cliente


class Menu:
    """
    Menu inicial do Sistema Bancário
    """
    lista_clientes: list = []
    lista_bancos: list = []
    lista_pessoas: list = []
    nomes_clientes: list = []

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

    def menu_cliente(self):
        for i, pessoa in enumerate(self.lista_pessoas):
            print(f"[{i}] {pessoa.nome}")
            self.nomes_clientes.append(pessoa.nome.upper())
        opcao = int(
            input(f"Deseja selecionar qual cliente? [999 para voltar] "))
        if opcao == 999:
            self.menu()
        print(f"""
                    ACESSO DO CLIENTE
                            Cliente selecionado: {self.nomes_clientes[opcao].upper()}

                            Escolha a opção desejada:
                                1 - Listar minhas contas bancárias
                                2 - Efetuar Depósito
                                3 - Efetuar Saque
                                4 - Efetuar Transferência
                                5 - Obter Extrato
                                6 - Voltar Menu Anterior
                            """)
        while True:
            escolha = int(input("Sua opção: "))
            if escolha not in range(1, 7):
                print("Escolha inválida. Tente novamente!")
            else:
                if escolha == 1:
                    pass
                elif escolha == 2:
                    c = Cliente(self.nomes_clientes[opcao].upper())
                    valor_deposito = float(
                        input("Qual valor deseja depositar? "))
                    c.deposito(valor_deposito)
                    c.saldo()
                elif escolha == 3:
                    pass
                elif escolha == 4:
                    pass
                elif escolha == 5:
                    pass
                elif escolha == 6:
                    self.menu_cliente()
                else:
                    print("Escolha inválida. Tente novamente!")

    def menu_pessoa(self):
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
        while True:
            escolha = int(input("Sua opção: "))
            if escolha not in range(1, 7):
                print("Escolha inválida. Tente novamente!")
            else:
                if escolha == 1:
                    nome = str(input("Informe o nome da pessoa: ").upper())
                    cpf = str(input("Informe o CPF da pessoa: "))
                    idade = int(input("Informe a idade da pessoa: "))
                    new_pessoa = Pessoa(nome=nome, cpf=cpf, idade=idade)
                    self.lista_pessoas.append(new_pessoa)
                    for i, pessoa in enumerate(self.lista_pessoas):
                        self.nomes_clientes.append(pessoa.nome.upper())
                elif escolha == 2:
                    for i, pessoa in enumerate(self.lista_pessoas):
                        print(f"[{i}] {pessoa.nome}")
                elif escolha == 3:
                    pes_pessoa = input(
                        "Qual pessoa deseja pesquisar? ").upper()
                    if (pes_pessoa in self.nomes_clientes) == True:
                        print(
                            f"A pessoa {pes_pessoa.upper()} se encontra na lista de pessoas do sistema.")
                    else:
                        print(
                            f"A pessoa {pes_pessoa.upper()} NÃO se encontra na lista de pessoas do sistema.")
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
