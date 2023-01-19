from sistema.sistema import Sistema


class Menu:
    """
    Menu inicial do Sistema Bancário
    """

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
                self.administrar_sistema()
            elif escolha == 2:
                self.acessar_como_cliente()
            elif escolha == 3:
                self.sair()
            else:
                print("Escolha inválida. Tente novamente!")

    def administrar_sistema(self):
        s = Sistema()
        return s.menu_principal()

    def acessar_como_cliente(self):
        pass

    def sair(self):
        print("Saindo do programa...")
        exit()
