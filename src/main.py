from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session
import models
from auth import api_key_auth
from database import get_db
import schemas

app = FastAPI()


@app.get("/", tags=["Check API status"])
def index():
    return {"status": "Healthy"}


@app.get("/students", dependencies=[Depends(api_key_auth)], tags=["List all students"], response_model=list[schemas.Student])
async def read_students(offset: int = 0, limit: int = 15, db: Session = Depends(get_db)) -> list[schemas.Student]:
    """
    List all students
    """
    students = db.execute(
        select(models.Student).offset(offset).limit(limit)).all()
    if not students:
        raise HTTPException(status_code=404, detail="Student not found")
    return students


@app.get("/registry", dependencies=[Depends(api_key_auth)], tags=["View registry"], response_model=list[schemas.Student])
async def read_students(offset: int = 0, limit: int = 15, db: Session = Depends(get_db)) -> list[schemas.Registry]:
    """
    Return student registry
    """
    registry = db.execute(
        select(models.Registry).offset(offset).limit(limit)).all()
    if not registry:
        raise HTTPException(status_code=404, detail="Registry not found")
    return registry
