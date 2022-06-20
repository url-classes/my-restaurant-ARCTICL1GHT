from buildham import BuildHam
from hamburguesa import Hamburguesa


class Director:
    def __init__(self):
        self.hamburguesa: Hamburguesa = BuildHam()

    def hamburguresa(self):
        self.hamburguesa.getresult()
        return self.hamburguesa.gettime()

    def getprice(self):
        return self.hamburguesa.getprice()

    def makehamburguesa(self, type: str):
        if "Queso" == type:
            self.hamburguesa.panstep()
            self.hamburguesa.carnestep()
            self.hamburguesa.quesostep()
            self.hamburguesa.mayonesastep()
            self.hamburguesa.ketpchupstep()
            self.hamburguesa.cebollastep()
            self.hamburguesa.panstep()
            return print()
        if "Tocino" == type:
            self.hamburguesa.panstep()
            self.hamburguesa.carnestep()
            self.hamburguesa.tocinostep()
            self.hamburguesa.mayonesastep()
            self.hamburguesa.ketpchupstep()
            self.hamburguesa.tomatestep()
            self.hamburguesa.cebollastep()
            self.hamburguesa.panstep()
        if "QuesoTocino" == type:
            self.hamburguesa.panstep()
            self.hamburguesa.carnestep()
            self.hamburguesa.quesostep()
            self.hamburguesa.mayonesastep()
            self.hamburguesa.ketpchupstep()
            self.hamburguesa.tocinostep()
            self.hamburguesa.tomatestep()
            self.hamburguesa.cebollastep()
            self.hamburguesa.panstep()
        if "QuesoDoble" == type:
            self.hamburguesa.panstep()
            self.hamburguesa.carnestep()
            self.hamburguesa.quesostep()
            self.hamburguesa.mayonesastep()
            self.hamburguesa.ketpchupstep()
            self.hamburguesa.tomatestep()
            self.hamburguesa.cebollastep()
            self.hamburguesa.panstep()
            self.hamburguesa.carnestep()
            self.hamburguesa.quesostep()
            self.hamburguesa.panstep()
        if "Simple" == type:
            self.hamburguesa.panstep()
            self.hamburguesa.carnestep()
            self.hamburguesa.tomatestep()
            self.hamburguesa.mayonesastep()
            self.hamburguesa.ketpchupstep()
            self.hamburguesa.cebollastep()
            self.hamburguesa.panstep()
