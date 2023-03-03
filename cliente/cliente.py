from pessoas.pessoas import Pessoa


class Cliente():
    """
    Classe para gerir as informações dos clientes.
    """

    pessoa: Pessoa
    contas: list = []

    def __init__(self, pessoa: Pessoa) -> None:
        self.pessoa = pessoa

    def criar_conta(self):
        from conta.conta import Conta
        nova_conta = Conta(str(input("Nome do banco: ").upper()))
        self.contas.append(nova_conta)

    def __str__(self) -> str:
        return f"Nome: {self.pessoa.nome} | CPF: {self.pessoa.cpf} | Idade: {self.pessoa.idade}"
