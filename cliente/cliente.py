from conta.conta import Conta
from pessoas.pessoas import Pessoa


class Cliente():
    """
    Classe para gerir as informações dos clientes.
    """

    pessoa: Pessoa
    contas: list = list()

    def __init__(self, pessoa: Pessoa, contas=[]) -> None:
        self.pessoa = pessoa
        self.contas = contas

    def vincular_conta(self, nova_conta: Conta):
        if len(self.contas) <= 0:
            self.contas = list()
        self.contas.append(nova_conta)

    def __str__(self) -> str:
        return f"Nome: {self.pessoa.nome} | CPF: {self.pessoa.cpf} | Idade: {self.pessoa.idade}"
