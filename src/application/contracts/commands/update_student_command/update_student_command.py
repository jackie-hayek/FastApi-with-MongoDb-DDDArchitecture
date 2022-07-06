from abc import ABC, abstractmethod, ABCMeta

from src.domain.models.student_model import Student as StudentsModel


class AbstractUpdateStudentCommand(ABC):
    __metaclass__ = ABCMeta

    @abstractmethod
    def handle(self, student_id: str, student: StudentsModel):
        raise NotImplementedError
