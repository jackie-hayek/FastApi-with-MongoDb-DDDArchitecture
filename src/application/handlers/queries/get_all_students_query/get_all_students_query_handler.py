import logging

from src.application.contracts.queries.get_all_students_query.get_all_students_query import AbstractGetAllStudentsQuery
from src.domain.contracts.abstract_student_repository import AbstractStudentRepository


class GetAllStudentsQuery(AbstractGetAllStudentsQuery):

    def __init__(self, student_repository: AbstractStudentRepository):
        self.student_repository = student_repository

    def handle(self):
        try:
            return self.student_repository.get_students()
            logging.info('Students list returned')

        except Exception as e:
            logging.info('No Students List available')
            raise e

