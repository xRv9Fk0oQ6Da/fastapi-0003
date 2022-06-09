from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

students = {
    1: {
        "name": "John Doe",
        "age": 18,
        "year": "2020"
    }
}

class Students(BaseModel):
    name: str,
    age: int,
    year: str

class Updatestudent(BaseModel):
    name: Options[str] = None
    age: Optional[int] = None
    year: Optional[str] = None
