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
                    bancos.append(
                        input("Deseja adicionar qual banco? ").upper())
                elif escolha == 2:
                    print(f"Lista de bancos: {bancos}")
                elif escolha == 3:
                    pes_banco = input("Qual banco deseja pesquisar? ").upper()
                    if (pes_banco in bancos) == True:
                        print(
                            f"O banco {pes_banco.upper()} se encontra na lista de bancos do sistema.")
                    else:
                        print(
                            f"O banco {pes_banco.upper()} NÃO se encontra na lista de bancos do sistema.")
                elif escolha == 4:
                    print("-" * 30)
                    for i, b in enumerate(bancos):
                        print(f"[{i}]: {b}")
                    print("-" * 30)
                    excluir_banco = int(
                        input("Deseja excluir qual banco? "))
                    print(
                        f"Banco {bancos[excluir_banco]} foi removido com sucesso!")
                    del bancos[excluir_banco]
                    print(f"Nova lista de bancos: {bancos}")
                elif escolha == 5:
                    print("-" * 30)
                    for i, b in enumerate(bancos):
                        print(f"[{i}]: {b}")
                    print("-" * 30)
                    atualizar_banco = int(
                        input("Deseja atualizar qual banco? "))
                    bancos[atualizar_banco] = input(
                        f"Atualizar banco {bancos[atualizar_banco]} para: ").upper()
                    print(
                        f"Banco {bancos[atualizar_banco]} foi atualizado com sucesso!")
                    print(f"Nova lista de bancos: {bancos}")
                elif escolha == 6:
                    from sistema.sistema import Sistema
                    voltar = Sistema()
                    return voltar.menu_principal()
                else:
                    print("Escolha inválida. Tente novamente!")
