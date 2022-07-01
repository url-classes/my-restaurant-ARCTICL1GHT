from abc import ABCMeta
from abc import abstractmethod


class Menu(metaclass=ABCMeta):
    @abstractmethod
    def createcomp(self):
        raise NotImplementedError

    @abstractmethod
    def createbeb(self):
        raise NotImplementedError

    @abstractmethod
    def createpost(self):
        raise NotImplementedError

    @abstractmethod
    def pedido(self):
        raise NotImplementedError

    @abstractmethod
    def precio(self):
        return self.__precio

    @abstractmethod
    def tiempo(self):
        return self.__tiempo
