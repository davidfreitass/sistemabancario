import datetime


class Conta:
    """
    Classe para gerir as traansações de cada conta dos clientes.
    """

    transacoes: list = list()
    saldo:  float = 0.0
    banco: str

    def __init__(self, banco: str) -> None:
        self.banco = banco

    def deposito(self, valor: float) -> None:
        if len(self.transacoes) <= 0:
            self.transacoes = list()
        self.transacoes.append({"tipo": "credito", "valor": valor})
        self.saldo += valor

    def saque(self, valor: float) -> None:
        if len(self.transacoes) <= 0:
            self.transacoes = list()
        self.transacoes.append({"tipo": "debito", "valor": valor})
        if self.saldo < valor:
            frase = "Saldo insuficiente para realizar esta transação."
            print('='*len(frase))
            print(frase)
            print('='*len(frase))
        else:
            self.saldo -= valor
            frase2 = "Valor transferido com SUCESSO!"
            print('='*len(frase2))
            print(frase2)
            print('='*len(frase2))

    def extrato(self):
        print('=' * 60)
        print(f"| SALDO ATUAL:".ljust(0),
              f"{self.saldo:.2f} |".rjust(60 - len('| SALDO ATUAL:')))
        if len(self.transacoes) >= 1:
            print(f"| ÚLTIMA TRANSAÇÃO:".ljust(
                0), f"{self.transacoes[-1]} |".rjust(60 - len('| ÚLTIMA TRANSAÇÃO:')))
        else:
            print(f"| ÚLTIMA TRANSAÇÃO:".ljust(0), f"Não houve transações |".rjust(
                60 - len('| ÚLTIMA TRANSAÇÃO:')))
        print(f"| DATA/HORA:".ljust(0),
              f"{datetime.datetime.now().ctime()} |".rjust(60 - len('| DATA/HORA:')))
        print('=' * 60)
