from dependency_injector import containers, providers

from src.application.contracts.queries.get_student_query.get_student_query import AbstractGetStudentByIdQuery
from src.application.handlers.queries.get_student_query.get_student_query_handler import GetStudentByIdQuery

from src.domain.contracts.abstract_student_repository import AbstractStudentRepository

from src.persistence.student_repository.student_repository import StudentRepository

from src.application.contracts.commands.add_student_command.add_student_command import AbstractAddStudentCommand
from src.application.handlers.commands.add_student_command.add_student_command_handler import AddStudentCommand

from src.application.contracts.commands.delete_student_command.delete_student_command import \
    AbstractDeleteStudentByIdCommand
from src.application.handlers.commands.delete_student_command.delete_student_command_handler import \
    DeleteStudentByIdCommand

from src.application.contracts.commands.update_student_command.update_student_command import \
    AbstractUpdateStudentCommand
from src.application.handlers.commands.update_student_command.update_student_command_handler import UpdateStudentCommand

from src.application.contracts.queries.get_all_students_query.get_all_students_query import AbstractGetAllStudentsQuery
from src.application.handlers.queries.get_all_students_query.get_all_students_query_handler import GetAllStudentsQuery


class PersistenceContainer(containers.DeclarativeContainer):
    student_repository = providers.Factory(AbstractStudentRepository.register(StudentRepository))


class ApplicationContainer(containers.DeclarativeContainer):
    add_student_command = providers.Factory(
        AbstractAddStudentCommand.register(AddStudentCommand),
        student_repository=PersistenceContainer.student_repository)

    delete_student_command = providers.Factory(
        AbstractDeleteStudentByIdCommand.register(DeleteStudentByIdCommand),
        student_repository=PersistenceContainer.student_repository)

    update_student_command = providers.Factory(
        AbstractUpdateStudentCommand.register(UpdateStudentCommand),
        student_repository=PersistenceContainer.student_repository)

    get_all_students_query = providers.Factory(
        AbstractGetAllStudentsQuery.register(GetAllStudentsQuery),
        student_repository=PersistenceContainer.student_repository)

    get_student_byId_query = providers.Factory(
        AbstractGetStudentByIdQuery.register(GetStudentByIdQuery),
        student_repository=PersistenceContainer.student_repository)
