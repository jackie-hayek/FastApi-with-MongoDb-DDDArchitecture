from fastapi import APIRouter, status

from src.dependency.containers import ApplicationContainer
from src.domain.models.student_model import Student as StudentsModel
from src.application.contracts.commands.update_student_command.update_student_response_model import UpdateStudentModel
import logging


router = APIRouter()

logging.basicConfig(level=logging.DEBUG)


@router.post("/student()", response_model=StudentsModel, status_code=status.HTTP_201_CREATED)
async def add_student(student: StudentsModel):
    return await ApplicationContainer.add_student_command().handle(student)


@router.get("/student()", response_model=list[StudentsModel], status_code=200)
async def get_students():
    return await ApplicationContainer.get_all_students_query().handle()


@router.get("/student/{student_id}", status_code=status.HTTP_200_OK)
async def get_student_by_id(student_id: str):
    return await ApplicationContainer.get_student_byId_command().handle(student_id)


@router.delete("/student/{student_id}", status_code=status.HTTP_200_OK)
async def delete_student_by_id(student_id: str):
    return await ApplicationContainer.delete_student_command().handle(student_id)


@router.put("/student/{student_id}", response_model=UpdateStudentModel, status_code=status.HTTP_200_OK)
async def update_student(student_id: str, studentx: UpdateStudentModel):
    return await ApplicationContainer.update_student_command().handle(student_id, studentx.dict())
