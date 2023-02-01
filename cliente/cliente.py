from pessoas.pessoas import Pessoa


class Cliente():
    """
    Menu de acesso dos clientes.
    """

    transacoes: list = {}
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

    def saldo(self) -> float:
        return self.saldo
