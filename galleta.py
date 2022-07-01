from postres import Postres


class Galleta(Postres):
    def __init__(self):
        self.__precio: float = 5
        self.__tiempo: float = 1

    def precio(self):
        return self.__precio

    def tiempo(self):
        return self.__tiempo
