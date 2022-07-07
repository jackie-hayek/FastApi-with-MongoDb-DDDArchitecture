from abc import ABC
from fastapi import HTTPException, status
from src.domain.contracts.abstract_student_repository import AbstractStudentRepository
from src.domain.models.student_model import Student as StudentsModel, Student
from typing import List, Union

from src.exceptions.exceptions import RepositoryException

student_collection = StudentsModel


class StudentRepository(AbstractStudentRepository):

    async def get_students(self) -> List[StudentsModel]:
        response = await student_collection.all().to_list()
        return response

    async def get_student_by_id(self, student_id: str):
        response = await student_collection.find_one(Student.student_id == student_id)
        return response

    async def add_new_student(self, studentx: StudentsModel):
        new_student = await studentx.create()
        return new_student

    async def delete_student_by_id(self, student_id: str) -> bool:
        student_to_delete = await student_collection.find_one(Student.student_id == student_id)

        if student_to_delete is None:
            raise RepositoryException(message='Student Not Found')
        else:
            await student_to_delete.delete()
            return True

    async def update_student_data(self, student_id: str, studentx: dict) -> Union[bool, StudentsModel]:
        des_body = {k: v for k, v in studentx.items() if v is not None}
        update_query = {"$set": {
            field: value for field, value in des_body.items()
        }}
        student_to_update = await student_collection.find_one(Student.student_id == student_id)
        if not student_to_update:
            raise RepositoryException(message='Student Not Found')
        else:
            await student_to_update.update(update_query)
            return student_to_update

