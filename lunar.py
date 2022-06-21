from director import Director
from menu import Menu
from complemento import Complemento
from papas import Papas
from bebida import Bebida
from cocacola import CocaCola
from postres import Postres
from helado import Helado


class Lunar(Menu):
    def __init__(self):
        self.__precio: float = 0
        self.__tiempo: float = 0

    def createcomp(self):
        papas: Complemento = Papas()
        self.__precio += papas.precio()
        self.__tiempo += papas.tiempo()

    def createbeb(self):
        coca: Bebida = CocaCola()
        self.__precio += coca.precio()
        self.__tiempo += coca.tiempo()

    def createpost(self):
        helado: Postres = Helado()
        self.__precio += helado.precio()
        self.__tiempo += helado.tiempo()

    def createham(self):
        hamburguesa: Director = Director()
        hamburguesa.quesomake()
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
