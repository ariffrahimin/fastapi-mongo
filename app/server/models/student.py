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
