from director import Director
from menu import Menu
from bebida import Bebida
from postres import Postres
from complemento import Complemento
from cocacola import CocaCola
from ensalada import Ensalada
from gelatina import Gelatina


class Venus(Menu):
    def __init__(self):
        self.__precio: float = 0
        self.__tiempo: float = 0

    def createcomp(self):
        complemento: Complemento = Ensalada()
        self.__precio += complemento.precio()
        self.__tiempo += complemento.tiempo()

    def createbeb(self):
        bebida: Bebida = CocaCola()
        self.__precio += bebida.precio()
        self.__tiempo += bebida.tiempo()

    def createpost(self):
        postre: Postres = Gelatina()
        self.__precio += postre.precio()
        self.__tiempo += postre.tiempo()

    def createham(self):
        hamburguesa: Director = Director()
        hamburguesa.tocinomake()
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
