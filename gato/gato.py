from animal.animal import Animal


class Gato(Animal):
    """
    Características e funções de um gato.
    """

    raça: str

    def __init__(self, nome: str, cor: str, sexo: str, raça: str) -> None:
        super().__init__(nome, cor, sexo)
        self.raça = raça

    def miar(self) -> None:
        print(f"{self.nome}: miauuuuuuuuu")

    def __str__(self) -> str:
        return f"O gato {self.nome} tem a cor {self.cor}, é {self.sexo} e é da raça {self.raça}."
