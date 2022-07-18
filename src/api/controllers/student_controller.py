import logging

from fastapi import APIRouter, status, HTTPException

from src.application.contracts.commands.add_student_command.add_student_command_request import AddStudentRequestModel
from src.application.contracts.commands.add_student_command.add_student_command_response import AddStudentResponseModel
from src.application.contracts.commands.update_student_command.update_student_response_model import UpdateStudentModel
from src.dependency.containers import ApplicationContainer
from src.exceptions.exceptions import Exceptions
from src.persistence.student_repository.student_model import Student as StudentsModel

router = APIRouter()

logging.basicConfig(level=logging.DEBUG)


@router.post("/student()", response_model=AddStudentResponseModel, status_code=status.HTTP_201_CREATED)
async def add_student(student: AddStudentRequestModel):
    try:
        return await ApplicationContainer.add_student_command().handle(student)
    except Exception as e:
        raise HTTPException(status_code=400, detail=e.__str__())
    except Exceptions as e:
        raise HTTPException(status_code=500, detail=e.__str__())


@router.get("/student()", response_model=list[StudentsModel], status_code=200)
async def get_students():
    return await ApplicationContainer.get_all_students_query().handle()


@router.get("/student/{student_id}", status_code=status.HTTP_200_OK)
async def get_student_by_id(student_id: str):
    return await ApplicationContainer.get_student_byId_query().handle(student_id)


@router.delete("/student/{student_id}", status_code=status.HTTP_200_OK)
async def delete_student_by_id(student_id: str):
    try:
        return await ApplicationContainer.delete_student_command().handle(student_id)
    except Exceptions as e:
        raise HTTPException(status_code=404, detail=e.__str__())
    except Exception as e:
        raise HTTPException(status_code=500, detail=e.__str__())


@router.put("/student/{student_id}", response_model=UpdateStudentModel, status_code=status.HTTP_200_OK)
async def update_student(student_id: str, studentx: UpdateStudentModel):
    try:
        return await ApplicationContainer.update_student_command().handle(student_id, studentx.dict())
    except Exceptions as e:
        raise HTTPException(status_code=404, detail=e.__str__())
    except ValueError as e:
        raise HTTPException(status_code=404, detail=e.__str__())
    except Exception as e:
        raise HTTPException(status_code=500, detail=e.__str__())