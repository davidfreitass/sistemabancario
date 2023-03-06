import datetime


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

    def extrato(self):
        print('=' * 60)
        print(f"| SALDO ATUAL:".ljust(0),
              f"{self.saldo:.2f} |".rjust(60 - len('| SALDO ATUAL:')))
        print(f"| ÚLTIMA TRANSAÇÃO:".ljust(0),
              f"{self.transacoes[-1]} |".rjust(60 - len('| Última transação:')))
        print(f"| DATA/HORA:".ljust(0),
              f"{datetime.datetime.now().ctime()} |".rjust(60 - len('| DATA/HORA:')))
        print('=' * 60)
