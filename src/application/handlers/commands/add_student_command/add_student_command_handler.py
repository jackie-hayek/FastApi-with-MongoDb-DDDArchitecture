import logging

from src.application.contracts.commands.add_student_command.add_student_command import AbstractAddStudentCommand
from src.application.contracts.commands.add_student_command.add_student_command_request import AddStudentRequestModel
from src.domain.contracts.abstract_student_repository import AbstractStudentRepository


class AddStudentCommand(AbstractAddStudentCommand):

    def __init__(self, student_repository: AbstractStudentRepository):
        self.student_repository = student_repository

    def handle(self, student: AddStudentRequestModel):
        new_student = self.student_repository.add_new_student(student)
        logging.info('Student added to the list')
        return new_student


