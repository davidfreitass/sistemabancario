class Menu:
    """
    Menu inicial do Sistema Bancário
    """

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
        else:
            break
