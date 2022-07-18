from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

from src.persistence.student_repository.student_model import Student


Mongo_Database = "mongodb://localhost:27017/FastAPI"


async def initiate_database():
    client = AsyncIOMotorClient(Mongo_Database)
    await init_beanie(database=client.FastAPI, document_models=[Student])
