from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session
from models import Student, Registry
from auth import api_key_auth
from database import get_db
from schemas import Student, Registry


app = FastAPI()


@app.get("/", tags=["Check API status"])
def index():
    return {"status": "Healthy"}


@app.get("/students", dependencies=[Depends(api_key_auth)], tags=["List all students"])
async def read_students(skip: int = 0, limit: int = 15, db: Session = Depends(get_db)) -> list[Student]:
    """
    List all students
    """
    students = db.execute(select(Student)).scalars().all()
    return students[skip: skip + limit]


@app.get("/registry", dependencies=[Depends(api_key_auth)], tags=["View registry"])
async def read_students(skip: int = 0, limit: int = 15, db: Session = Depends(get_db)) -> list[Registry]:
    """
    Return student registry
    """
    registry = db.execute(select(Registry)).scalars().all()
    return registry[skip: skip + limit]
