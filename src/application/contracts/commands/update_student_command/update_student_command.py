from abc import ABC, abstractmethod, ABCMeta

from src.application.contracts.commands.update_student_command.update_student_response_model import UpdateStudentModel


class AbstractUpdateStudentCommand(ABC):
    __metaclass__ = ABCMeta

    @abstractmethod
    def handle(self, student_id: str, student: UpdateStudentModel):
        raise NotImplementedError
