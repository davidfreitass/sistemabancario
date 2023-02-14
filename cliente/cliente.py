from pessoas.pessoas import Pessoa


class Cliente():
    """
    Classe para gerir as informações dos clientes.
    """

    transacoes: list = []
    saldo:  float = 0.0
    pessoa: Pessoa

    def __init__(self, pessoa: Pessoa) -> None:
        self.pessoa = pessoa

    def deposito(self, valor: float) -> None:
        self.transacoes.append({"tipo": "credito", "valor": valor})
        self.saldo += valor

    def saque(self, valor: float) -> None:
        self.transacoes.append({"tipo": "debito", "valor": valor})
        self.saldo -= valor

    def extrato(self) -> str:
        return f"SALDO ATUAL: {self.saldo:.2f}"

    def __str__(self) -> str:
        return f"Nome: {self.pessoa.nome} | CPF: {self.pessoa.cpf} | Idade: {self.pessoa.idade}"
