class Cliente:
    """
    Menu de acesso dos clientes.
    """

    def menu_cliente(self):
        from listas.listas import pessoas

        for i, p in enumerate(pessoas):
            print(f"[{i}]: {p.upper()}")
        opcao = int(input("Deseja selecionar qual cliente? "))
        print(f"""
                    ACESSO DO CLIENTE
                            Cliente selecionado: {pessoas[opcao].upper()}

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
                    pass
                elif escolha == 3:
                    pass
                elif escolha == 4:
                    pass
                elif escolha == 5:
                    pass
                elif escolha == 6:
                    pass
                else:
                    print("Escolha inválida. Tente novamente!")
