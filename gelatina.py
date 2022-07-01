from postres import Postres


class Gelatina(Postres):
    def __init__(self):
        self.__precio: float = 10
        self.__tiempo: float = 3

    def precio(self):
        return self.__precio

    def tiempo(self):
        return self.__tiempo
