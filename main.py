from fastapi import FastAPI, Path, Query
from typing import Optional

from . import application, models

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/students/{student_id}")
def get_student():
    res = application.read_student()
    return res


@app.get("/get-by-name/{student_id}")
def get_student_by_name(
    student_id: int = Path(..., description="The ID of the student you want to view"),
    name: Optional[str] = Query(None, description="The name of the student"),
):
    res = application.get_by_name(student_id=student_id, name=name)
    return res


@app.post("/create-student/{student_id}")
def create_student(
    student_id: int,
    student: models.Student,
):
    res = application.create_student(student_id=student_id, student=student)
    return res


@app.put("/update-student/{student_id}")
def update_student(
    student_id: int,
    student: models.UpdateStudent,
):
    res = application.update_student(student_id=student_id, student=student)
    return res


@app.delete("/delete-student/{student_id}")
def delete_student(
    student_id: int,
):
    res = application.delete_student(student_id=student_id)
    return res
