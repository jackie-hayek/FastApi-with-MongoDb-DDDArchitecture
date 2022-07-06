from abc import ABC, abstractmethod, ABCMeta


class AbstractGetAllStudentsQuery(ABC):
    __metaclass__ = ABCMeta

    @abstractmethod
    def handle(self):
        raise NotImplementedError
