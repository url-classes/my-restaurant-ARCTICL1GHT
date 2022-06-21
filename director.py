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

    def quesomake(self):
            self.hamburguesa.panstep()
            self.hamburguesa.carnestep()
            self.hamburguesa.quesostep()
            self.hamburguesa.mayonesastep()
            self.hamburguesa.ketpchupstep()
            self.hamburguesa.tomatestep()
            self.hamburguesa.cebollastep()
            self.hamburguesa.panstep()
            return print()

    def tocinomake(self):
            self.hamburguesa.panstep()
            self.hamburguesa.carnestep()
            self.hamburguesa.tocinostep()
            self.hamburguesa.mayonesastep()
            self.hamburguesa.ketpchupstep()
            self.hamburguesa.tomatestep()
            self.hamburguesa.cebollastep()
            self.hamburguesa.panstep()

    def quesotocinomake(self):
            self.hamburguesa.panstep()
            self.hamburguesa.carnestep()
            self.hamburguesa.quesostep()
            self.hamburguesa.mayonesastep()
            self.hamburguesa.ketpchupstep()
            self.hamburguesa.tocinostep()
            self.hamburguesa.tomatestep()
            self.hamburguesa.cebollastep()
            self.hamburguesa.panstep()

    def quesodoblemake(self):
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

    def simplemake(self):
            self.hamburguesa.panstep()
            self.hamburguesa.carnestep()
            self.hamburguesa.tomatestep()
            self.hamburguesa.mayonesastep()
            self.hamburguesa.ketpchupstep()
            self.hamburguesa.cebollastep()
            self.hamburguesa.panstep()
