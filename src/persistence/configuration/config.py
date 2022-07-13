from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseSettings

from src.domain.models.student_model import Student

Mongo_Database = "mongodb://localhost:27017/FastAPI"


class Settings(BaseSettings):
    # JWT
    secret_key: str
    algorithm: str = "RS256"

    class Config:
        env_file = ".env.dev"
        orm_mode = True


async def initiate_database():
    client = AsyncIOMotorClient(Mongo_Database)
    await init_beanie(database=client.FastAPI, document_models=[Student])
