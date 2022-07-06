from http.client import HTTPException

from src.application.contracts.commands.delete_student_command.delete_student_command import AbstractDeleteStudentByIdCommand
from src.domain.contracts.abstract_student_repository import AbstractStudentRepository
import logging


class DeleteStudentByIdCommand(AbstractDeleteStudentByIdCommand):
    def __init__(self, student_repository: AbstractStudentRepository):
        self.student_repository = student_repository

    def handle(self, id: str):
        deleted_student = self.student_repository.delete_student_by_id(id)
        if not deleted_student:
            logging.error('Student not found')
            raise HTTPException(status_code=404, detail="Student not found")
        logging.info('Student deleted')
        return deleted_student
