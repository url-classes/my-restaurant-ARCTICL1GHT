from abc import abstractmethod
from abc import ABCMeta


class Complemento(metaclass=ABCMeta):
    @abstractmethod
    def precio(self):
        raise NotImplementedError

    @abstractmethod
    def tiempo(self):
        raise NotImplementedError
