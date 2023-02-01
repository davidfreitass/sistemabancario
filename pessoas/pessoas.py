class Pessoa:
    """
    Menu de gerenciamento de pessoas.
    """

    nome: str
    cpf: str
    idade: int

    def __init__(self, nome: str, cpf: str, idade: int) -> None:
        self.nome = nome
        self.cpf = cpf
        self.idade = idade
