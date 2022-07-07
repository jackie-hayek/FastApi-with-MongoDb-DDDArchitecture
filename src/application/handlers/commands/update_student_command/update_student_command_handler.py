import logging

from src.application.contracts.commands.update_student_command.update_student_command import \
    AbstractUpdateStudentCommand
from src.application.contracts.commands.update_student_command.update_student_response_model import UpdateStudentModel
from src.domain.contracts.abstract_student_repository import AbstractStudentRepository


class UpdateStudentCommand(AbstractUpdateStudentCommand):
    def __init__(self, student_repository: AbstractStudentRepository):
        self.student_repository = student_repository

    def handle(self, id: str, student: UpdateStudentModel):
        try:
            updated_student = self.student_repository.update_student_data(id, student)
            logging.info('Student data updated')
            return updated_student

        except ValueError as e:
            raise e

        except Exception as e:
            logging.error('Student not found')
            raise e
