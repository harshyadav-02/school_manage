from typing import Optional
from pydantic import BaseModel, ConfigDict


class StudentCreate(BaseModel):
    name: str
    email: str
    age: int
    student_class: str


class StudentUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    age: Optional[int] = None
    student_class: Optional[str] = None


class StudentResponse(StudentCreate):
    id: int
    model_config = ConfigDict(from_attributes=True)