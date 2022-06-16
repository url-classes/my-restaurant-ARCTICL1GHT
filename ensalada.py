from complemento import Complemento


class Ensalada(Complemento):
    def __init__(self):
        self.__precio: float = 8
        self.__tiempo: float = 5

    def precio(self):
        return self.__precio

    def tiempo(self):
        return self.__tiempo
