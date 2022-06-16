from abc import ABCMeta
from abc import abstractmethod


class Postres(metaclass=ABCMeta):
    @abstractmethod
    def precio(self):
        raise NotImplementedError

    def tiempo(self):
        raise NotImplementedError
