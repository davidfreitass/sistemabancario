class Pessoa:
    """
    Classe para gerir as informações de uma pessoa.
    """

    nome: str
    cpf: str
    idade: int

    def __init__(self, nome: str, cpf: str, idade: int) -> None:
        self.nome = nome
        self.cpf = cpf
        self.idade = idade

    def __str__(self) -> str:
        return f"Nome: {self.nome} | CPF: {self.cpf} | Idade: {self.idade}"
