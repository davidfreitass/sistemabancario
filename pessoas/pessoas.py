class Pessoa:
    """
    Menu de gerenciamento de pessoas.
    """

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
                    from sistema.sistema import Sistema
                    voltar = Sistema()
                    return voltar.menu_principal()
                else:
                    print("Escolha inválida. Tente novamente!")
