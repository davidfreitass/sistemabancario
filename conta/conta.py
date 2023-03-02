from cliente.cliente import Cliente


class Conta:
    """
    Classe para gerir as traansações de cada conta dos clientes.
    """

    transacoes: list = []
    saldo:  float = 0.0
    banco: str

    def __init__(self, banco: str) -> None:
        self.banco = banco

    def deposito(self, valor: float) -> None:
        self.transacoes.append({"tipo": "credito", "valor": valor})
        self.saldo += valor

    def saque(self, valor: float) -> None:
        self.transacoes.append({"tipo": "debito", "valor": valor})
        self.saldo -= valor

    def extrato(self) -> str:
        return f"SALDO ATUAL: {self.saldo:.2f}"
