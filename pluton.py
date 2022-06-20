from director import Director
from menu import Menu
from bebida import Bebida
from postres import Postres
from complemento import Complemento
from galleta import Galleta
from te import Te
from ensalada import Ensalada


class Pluton(Menu):
    def __init__(self):
        self.__precio: float = 0
        self.__tiempo: float = 0

    def createcomp(self):
        papas: Complemento = Ensalada()
        self.__precio += papas.precio()
        self.__tiempo += papas.tiempo()

    def createbeb(self):
        coca: Bebida = Te()
        self.__precio += coca.precio()
        self.__tiempo += coca.tiempo()

    def createpost(self):
        helado: Postres = Galleta()
        self.__precio += helado.precio()
        self.__tiempo += helado.tiempo()

    def createham(self):
        hamburguesa: Director = Director()
        hamburguesa.makehamburguesa("Tocino")
        self.__tiempo += hamburguesa.hamburguresa()
        self.__precio += hamburguesa.getprice()

    def pedido(self):
        self.createcomp()
        self.createbeb()
        self.createpost()
        self.createham()

    def precio(self):
        return self.__precio

    def tiempo(self):
        return self.__tiempo
