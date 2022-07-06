from abc import ABC, abstractmethod, ABCMeta


class AbstractGetStudentByIdQuery(ABC):
    __metaclass__ = ABCMeta

    @abstractmethod
    def handle(self, student_id: str):
        raise NotImplementedError
