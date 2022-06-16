from bebida import Bebida


class CocaCola(Bebida):
    def __init__(self):
        self.__precio: float = 10.25

    def precio(self):
        return self.__precio

    def tiempo(self):
        return 0
