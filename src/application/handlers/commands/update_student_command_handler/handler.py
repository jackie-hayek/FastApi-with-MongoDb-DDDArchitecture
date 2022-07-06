from fastapi import HTTPException

import logging

from src.application.contracts.commands.update_student_command.update_student_command import AbstractUpdateStudentCommand
from src.domain.contracts.abstract_student_repository import AbstractStudentRepository
from src.domain.models.student_model import Student as StudentsModel


class UpdateStudentCommand(AbstractUpdateStudentCommand):
    def __init__(self, student_repository: AbstractStudentRepository):
        self.student_repository = student_repository

    def handle(self, id: str, student: StudentsModel):
        updated_student = self.student_repository.update_student_data(id, student)
        if not updated_student:
            logging.error('Student not found')
            raise HTTPException(status_code=404, detail="Student not found")
        logging.info('Student data updated')
        return updated_student
