import uvicorn
from fastapi import FastAPI, Depends
from src.api.controllers.student_controller import router as StudentRouter
from src.api.controllers.admin_controller import router as AdminRouter
from src.api.auth.jwt_bearer import JWTBearer
from src.persistence.configuration.config import initiate_database

app = FastAPI()

token_listener = JWTBearer()


@app.on_event("startup")
async def start_database():
    await initiate_database()


app.include_router(AdminRouter, tags=["Administrator"], prefix="/admin")
app.include_router(StudentRouter, tags=["Students"], prefix="/student", dependencies=[Depends(token_listener)])

if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8000, reload=True)
