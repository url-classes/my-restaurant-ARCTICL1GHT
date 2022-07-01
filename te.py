from bebida import Bebida


class Te(Bebida):
    def __init__(self):
        self.__precio: float = 10
        self.__tiempo: int = 3

    def precio(self):
        return self.__precio

    def tiempo(self):
        return self.__tiempo
