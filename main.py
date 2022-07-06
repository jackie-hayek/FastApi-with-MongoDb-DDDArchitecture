import uvicorn
from fastapi import FastAPI
from src.api.controllers.student_controller import router as StudentRouter
from src.persistence.configuration.config import initiate_database

app = FastAPI()


@app.on_event("startup")
async def start_database():
    await initiate_database()


app.include_router(StudentRouter, tags=["Students"], prefix="/student")

if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8000, reload=True)
