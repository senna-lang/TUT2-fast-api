from fastapi import Path
from typing import Optional
from . import models


students = {
    1: {"name": "John", "age": 17, "year": "year 12"},
    2: {"name": "Jane", "age": 18, "year": "year 12"},
}


def read_student(
    student_id: int = Path(
        None,
        description="The ID of the student you want to view",
        gt=0,  # descriptionはSwaggerUIに表示される　gt=0で0より大きい整数を受け取る
    ),
):
    return students[student_id]


def get_by_name(
    *, student_id: int, name: Optional[str] = None
):  # *でキーワード引数のみを受け取る　get_student(name="John")のように呼び出す
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    return {"Data": "Not found"}


def create_student(student_id: int, student: models.Student):
    if student_id in students:
        return {"Error": "Student already exists"}

    students[student_id] = student
    return student[student_id]


def update_student(student_id: int, student: models.UpdateStudent):
    if student_id not in students:
        return {"Error": "Student does not exist"}

    if student.name is not None:
        students[student_id].name = student.name

    if student.age is not None:
        students[student_id].age = student.age

    if student.year is not None:
        students[student_id].year = student.year

    return students[student_id]


def delete_student(student_id: int):
    if student_id not in students:
        return {"Error": "Student does not exist"}

    del students[student_id]
    return {"Message": "Student deleted"}