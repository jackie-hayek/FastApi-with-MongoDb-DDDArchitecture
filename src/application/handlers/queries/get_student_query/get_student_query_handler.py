import logging

from src.application.contracts.queries.get_student_query.get_student_query import AbstractGetStudentByIdQuery
from src.domain.contracts.abstract_student_repository import AbstractStudentRepository


class GetStudentByIdQuery(AbstractGetStudentByIdQuery):

    def __init__(self, student_repository: AbstractStudentRepository):
        self.student_repository = student_repository

    def handle(self, student_id: str):
        try:
            return self.student_repository.get_student_by_id(student_id)
            logging.info('Student with the specified id is returned')
        except Exception as e:
            logging.error('Student with the specified id is not found')
            raise e
