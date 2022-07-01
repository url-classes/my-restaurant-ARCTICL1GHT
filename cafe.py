from bebida import Bebida


class Cafe(Bebida):
    def __init__(self):
        self.__precio: float = 12.50
        self.__tiempo: int = 4

    def precio(self):
        return self.__precio

    def tiempo(self):
        return self.__tiempo
