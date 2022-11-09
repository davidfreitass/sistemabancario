class Sistema:
    """
    Menu de administração do Sistema
    """

    print("""
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
            break
