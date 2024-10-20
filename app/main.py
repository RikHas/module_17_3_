from fastapi import FastAPI
from app.routers.task import router as task_router
from app.routers.user import router as user_router
from app.models import User, Task
from sqlalchemy.schema import CreateTable


app = FastAPI()


@app.get("/")
async def welcome():
    return {"message": "Welcome to Taskmanager"}

app.include_router(user_router)
app.include_router(task_router)


print(CreateTable(Task.__table__))
print(CreateTable(User.__table__))
