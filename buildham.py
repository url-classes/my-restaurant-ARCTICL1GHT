from abc import ABC

from ham import Ham
from hamburguesa import Hamburguesa


class BuildHam(Hamburguesa, ABC):
    def __init__(self):
        self.resultado: Ham = Ham()

    def getprice(self):
        return self.resultado.getprice()

    def reset(self):
        self.resultado = Ham()
        return ""

    def panstep(self):
        self.resultado.addpan()
        return ""

    def carnestep(self):
        self.resultado.addcarne()
        return ""

    def ketpchupstep(self):
        self.resultado.addketchup()
        return ""

    def mayonesastep(self):
        self.resultado.addmayonesa()
        return ""

    def gettime(self):
        return self.resultado.gettime()

    def tocinostep(self):
        self.resultado.addtocino()
        return ""

    def quesostep(self):
        self.resultado.addqueso()
        return ""

    def cebollastep(self):
        self.resultado.addcebolla()
        return ""

    def tomatestep(self):
        self.resultado.addtomate()
        return ""

    def getresult(self):
        return self.resultado.getresult()
