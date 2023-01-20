class Banco:
    """
    Menu de gerenciamento de bancos.
    """

    def menu_banco(self):
        from listas.listas import bancos

        print("""
            GERENCIAR BANCOS
                Escolha a opção desejada:
                    1 - Novo Banco
                    2 - Listar Bancos
                    3 - Pesquisar Banco
                    4 - Excluir Banco
                    5 - Atualizar Banco
                    6 - Voltar Menu Anterior
        """)
        while True:
            escolha = int(input("Sua opção: "))
            if escolha not in range(1, 7):
                print("Escolha inválida. Tente novamente!")
            else:
                if escolha == 1:
                    bancos.append(input("Deseja adicionar qual banco? "))
                elif escolha == 2:
                    print(f"Lista de bancos: {bancos}")
                elif escolha == 3:
                    pass
                elif escolha == 4:
                    pass
                elif escolha == 5:
                    pass
                elif escolha == 6:
                    from sistema.sistema import Sistema
                    voltar = Sistema()
                    return voltar.menu_principal()
                else:
                    print("Escolha inválida. Tente novamente!")
