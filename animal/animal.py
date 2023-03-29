class Animal:
    """
    Características e funções de um animal.
    """

    nome: str
    cor: str
    sexo: str

    def __init__(self, nome: str, cor: str, sexo: str) -> None:
        self.nome = nome
        self.cor = cor
        self.sexo = sexo

    def comer(self) -> None:
        print(f"{self.nome} está comendo.")
