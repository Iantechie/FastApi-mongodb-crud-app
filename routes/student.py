from fastapi import APIRouter
from models.student import Student # Student Model
from config.database import connection #db connection
from schemas.student import StudentEntity, ListOfStudentEntity
from bson import ObjectId



student_router = APIRouter()

#endpoints
@student_router.get('/hello')
async def hello_world():
    return "Hello FastApi"


#getting all students
@student_router.get('/students')
async def find_all_students():
    return ListOfStudentEntity(connection.local.student.find())

#create a student
@student_router.post('/students')
async def create_student(student: Student):
    connection.local.student.insert_one(dict(student))
    return ListOfStudentEntity(connection.local.student.find())

#update a student(s)
@student_router.put('/students/{studentId}')
async def update_student(studentId, student:Student):
    connection.local.student.find_one_and_update(
        {"_id":ObjectId(studentId) },
        {"$set":dict(student)}
    )
    return connection.local.find_one({"_id":ObjectId(studentId)})

#delete a student
@student_router.delete('/students/{studentId}')
async def delte_student(studentId):
   return StudentEntity(connection.local.student.find_one_and_delete({"_id": ObjectId(studentId)}))
