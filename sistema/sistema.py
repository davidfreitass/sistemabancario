class Sistema:
    """
    Menu de administração do Sistema
    """

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
                    self.gerenciar_bancos()
                elif escolha == 2:
                    self.gerenciar_pessoas()
                elif escolha == 3:
                    self.gerenciar_agencias()
                elif escolha == 4:
                    self.gerenciar_contas()
                elif escolha == 5:
                    from menu.menu import Menu
                    voltar = Menu()
                    return voltar.menu()
                else:
                    print("Escolha inválida. Tente novamente!")

    def gerenciar_bancos(self):
        from banco.banco import Banco
        b = Banco()
        return b.menu_banco()

    def gerenciar_pessoas(self):
        from pessoas.pessoas import Pessoa
        p = Pessoa()
        return p.menu_pessoa()

    def gerenciar_agencias(self):
        pass

    def gerenciar_contas(self):
        pass
