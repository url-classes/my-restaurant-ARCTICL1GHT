from abc import ABCMeta
from abc import abstractmethod


class Bebida(metaclass=ABCMeta):

    @abstractmethod
    def precio(self):
        raise NotImplementedError

    @abstractmethod
    def tiempo(self):
        raise NotImplementedError
