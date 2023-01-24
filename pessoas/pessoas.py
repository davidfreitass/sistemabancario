class Pessoa:
    """
    Menu de gerenciamento de pessoas.
    """

    def menu_pessoa(self):
        from listas.listas import pessoas

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
                    pessoas.append(
                        input("Deseja adicionar que pessoa? ").upper())
                elif escolha == 2:
                    print(f"Lista de pessoas: {pessoas}")
                elif escolha == 3:
                    pes_pessoa = input(
                        "Qual pessoa deseja pesquisar? ").upper()
                    if (pes_pessoa in pessoas) == True:
                        print(
                            f"A pessoa {pes_pessoa.upper()} se encontra na lista de pessoas do sistema.")
                    else:
                        print(
                            f"A pessoa {pes_pessoa.upper()} NÃO se encontra na lista de pessoas do sistema.")
                elif escolha == 4:
                    print("-" * 30)
                    for i, p in enumerate(pessoas):
                        print(f"[{i}]: {p}")
                    print("-" * 30)
                    excluir_pessoa = int(
                        input("Deseja excluir qual pessoa? "))
                    print(
                        f"A pessoa {pessoas[excluir_pessoa]} foi removida com sucesso!")
                    del pessoas[excluir_pessoa]
                    print(f"Nova lista de pessoas: {pessoas}")
                elif escolha == 5:
                    print("-" * 30)
                    for i, b in enumerate(pessoas):
                        print(f"[{i}]: {b}")
                    print("-" * 30)
                    atualizar_pessoa = int(
                        input("Deseja atualizar qual pessoa? "))
                    pessoas[atualizar_pessoa] = input(
                        f"Atualizar pessoa {pessoas[atualizar_pessoa]} para: ").upper()
                    print(
                        f"A pessoa {pessoas[atualizar_pessoa]} foi atualizada com sucesso!")
                    print(f"Nova lista de pessoas: {pessoas}")
                elif escolha == 6:
                    from sistema.sistema import Sistema
                    voltar = Sistema()
                    return voltar.menu_principal()
                else:
                    print("Escolha inválida. Tente novamente!")
