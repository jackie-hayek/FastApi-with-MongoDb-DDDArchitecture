from src.application.contracts.commands.delete_student_command.delete_student_command import \
    AbstractDeleteStudentByIdCommand
from src.domain.contracts.abstract_student_repository import AbstractStudentRepository
import logging
from src.exceptions.exceptions import Exceptions


class DeleteStudentByIdCommand(AbstractDeleteStudentByIdCommand):
    def __init__(self, student_repository: AbstractStudentRepository):
        self.student_repository = student_repository

    def handle(self, id: str):
        try:
            deleted_student = self.student_repository.delete_student_by_id(id)
            return deleted_student
            logging.info('Student deleted')

        except Exceptions as e:
            logging.error('Student not found')
            raise e

        except Exception as e:
            raise e
