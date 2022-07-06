from abc import ABC, abstractmethod, ABCMeta

from src.application.contracts.commands.add_student_command.add_student_command_request import AddStudentRequestModel


class AbstractAddStudentCommand(ABC):
    __metaclass__ = ABCMeta

    @abstractmethod
    def handle(self, student: AddStudentRequestModel):
        raise NotImplementedError
