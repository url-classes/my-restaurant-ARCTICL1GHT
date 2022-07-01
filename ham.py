class Ham:
    def __init__(self):
        self.__pan: int = 0
        self.__carne: int = 0
        self.__ketpchup: int = 0
        self.__mayonesa: int = 0
        self.__tocino: int = 0
        self.__queso: int = 0
        self.__cebolla: int = 0
        self.__tomate: int = 0
        self.__time: int = 0
        self.__price: float = 0

    def addpan(self):
        self.__pan += 1
        self.__time += 8
        self.__price += 10

    def addcarne(self):
        self.__carne += 1
        self.__time += 6
        self.__price += 12

    def addketchup(self):
        self.__ketpchup += 1
        self.__time += 4
        self.__price += 1.5

    def addmayonesa(self):
        self.__mayonesa += 1
        self.__time += 6
        self.__price += 1.5

    def addtocino(self):
        self.__tocino += 1
        self.__time += 5
        self.__price += 8

    def addqueso(self):
        self.__queso += 1
        self.__time += 3
        self.__price += 3

    def addcebolla(self):
        self.__cebolla += 1
        self.__time += 3
        self.__price += 2

    def addtomate(self):
        self.__tomate += 1
        self.__time += 3
        self.__price += 2

    def getprice(self):
        return self.__price

    def getresult(self):
        return print(f"Pan: {self.__pan} - Queso: {self.__queso} - Tomate: {self.__tomate} -"
                     f" Cebolla: {self.__cebolla}\nMayonesa: {self.__mayonesa} - Carne: {self.__carne} -"
                     f" Ketchup: {self.__ketpchup} - Tocino: {self.__tocino}")

    def gettime(self):
        return self.__time
