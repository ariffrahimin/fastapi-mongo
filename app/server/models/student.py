from typing import Optional
from pydantic import BaseModel, EmailStr, Field


class StudentSchema(BaseModel):
    fullname: str = Field(...)
    email: EmailStr = Field(...)
    course_of_study: str = Field(...)
    year: int = Field(..., gt=0, lt=9)
    gpa: float = Field(..., le=4.0)

    class Config:
        schema_extra = {
            "example": {
                "fullname": "Ariff Rahimin Bin Mohamed Norazman",
                "email": "ariffrahiminmohamed@airasia.com",
                "course_of_study": "Bachelor Of Computer Science (Artificial Intelligence)",
                "year": 4,
                "gpa": 3.97
            }
        }


class UpdateStudentModel(BaseModel):
    fullname: Optional[str]
    email: Optional[EmailStr]
    course_of_study: Optional[str]
    year: Optional[int]
    gpa: Optional[float]

    class Config:
        schema_extra = {
            "example": {
                "fullname": "Roman Dimitry",
                "email": "romancairo@gmail.com",
                "course_of_study": "Swordmanship and Noble Studies",
                "year": 3,
                "gpa": 4.00
            }
        }


def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message

    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}
