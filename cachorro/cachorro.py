from animal.animal import Animal


class Cachorro(Animal):
    """
    Características e funções de um cachorro.
    """

    peso: float

    def __init__(self, nome: str, cor: str, sexo: str, peso: float) -> None:
        super().__init__(nome, cor, sexo)
        self.peso = peso

    def latir(self) -> None:
        print(f"{self.nome}: au au au")

    def __str__(self) -> str:
        return f"O cachorro {self.nome} tem a cor {self.cor}, é {self.sexo} e pesa {self.peso} kgs."
