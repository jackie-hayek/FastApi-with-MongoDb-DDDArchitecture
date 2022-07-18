from abc import ABC, abstractmethod, ABCMeta

from src.application.contracts.commands.add_student_command.add_student_command_request import AddStudentRequestModel
from src.persistence.student_repository.student_model import Student as StudentsModel


class AbstractStudentRepository(ABC):
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_students(self):
        raise NotImplementedError

    @abstractmethod
    def get_student_by_id(self, student_id: str):
        raise NotImplementedError

    @abstractmethod
    async def add_new_student(self, studentx: AddStudentRequestModel):
        raise NotImplementedError

    @abstractmethod
    def delete_student_by_id(self, student_id: str):
        raise NotImplementedError

    @abstractmethod
    def update_student_data(self, student_id: str, studentx: StudentsModel):
        raise NotImplementedError
