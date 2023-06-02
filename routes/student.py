from fastapi import APIRouter
from models.student import Student # Student Model
from config.database import connection #db connection

student_router = APIRouter()

#endpoints
@student_router.get('/hello')
async def hello_world():
    return "Hello FastApi"

@student_router.get('/students')
async def find_all_students():
    return connection.local.student.find()
