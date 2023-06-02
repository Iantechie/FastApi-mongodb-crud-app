from fastapi import FastAPI
from routes.student import student_router

#create app
app = FastAPI()
#register routes
app.include_router(student_router)