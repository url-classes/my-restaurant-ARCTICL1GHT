from complemento import Complemento


class Papas(Complemento):
    def __init__(self):
        self.__precio: float = 15
        self.__tiempo: float = 6

    def precio(self):
        return self.__precio

    def tiempo(self):
        return self.__tiempo
