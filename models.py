from pydantic import BaseModel
from typing import Optional


class Student(BaseModel):
    name: str
    age: int
    year: int


class UpdateStudent:
    name: Optional[str] = None
    age: Optional[int] = None
    year: Optional[str] = None


