from fastapi import HTTPException

import logging

from src.application.contracts.queries.get_student_query.get_student_query import AbstractGetStudentByIdQuery
from src.domain.contracts.abstract_student_repository import AbstractStudentRepository


class GetStudentByIdQuery(AbstractGetStudentByIdQuery):

    def __init__(self, student_repository: AbstractStudentRepository):
        self.student_repository = student_repository

    def handle(self, student_id: str):
        student = self.student_repository.get_student_by_id(student_id)
        if not student:
            logging.error('Student with the specified id is not found')
            raise HTTPException(status_code=404, detail="Student not found")
        logging.info('Student with the specified id is returned')
        return student
