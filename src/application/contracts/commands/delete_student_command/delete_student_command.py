from abc import ABC, abstractmethod, ABCMeta


class AbstractDeleteStudentByIdCommand(ABC):
    __metaclass__ = ABCMeta

    @abstractmethod
    def handle(self, student_id: str):
        raise NotImplementedError
