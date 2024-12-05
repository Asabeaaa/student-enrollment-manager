from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.exc import SQLAlchemyError
import uvicorn
from sqlalchemy import select
from sqlalchemy.orm import Session
import models
from auth import api_key_auth
from database import get_db
from uuid import UUID
import schemas

app = FastAPI()


@app.get("/", tags=["Check API status"])
def index():
    return {"status": "Healthy"}


@app.get("/students/{student_id}", dependencies=[Depends(api_key_auth)], tags=["Get specific student"])
async def get_student_by_id(student_id: UUID, db: Session = Depends(get_db)):
    # Retrieve student from the database using the student_id
    student = db.query(models.Student).filter(
        models.Student.studentId == student_id).first()
    # Close the session
    db.close()
    if not student:
        raise HTTPException(
            status_code=404, detail="Student record not found")
    return student


@app.post("/students/onboard")
async def register_student(student: schemas.StudentCreate, db: Session = Depends(get_db)):
    # Create a new student object using the request data
    new_student = models.Student(studentId=student.student_id, firstName=student.first_name,
                                 otherNames=student.other_names, lastName=student.last_name,
                                 dateOfBirth=student.date_of_birth)
    # Add the student to the session
    db.add(new_student)
    # Commit the session to persist the changes
    try:
        db.commit()
        return student
    except SQLAlchemyError as e:
        if "duplicate key value violates unique constraint" in str(e):
            raise HTTPException(
                status_code=404, detail="Student id already exits")
    finally:
        # Close the session
        db.close()


@app.post("/students/register")
async def register_student(onboard_student: schemas.RegistryCreate, db: Session = Depends(get_db)):
    # Create a new registry object using the request data
    onboarded_student = models.Registry(registryId=onboard_student.registry_id, studentId=onboard_student.student_id,
                                        classId=onboard_student.class_id, status=onboard_student.status)
    # Add the student to the session
    db.add(onboarded_student)

    # Commit the session to persist the changes
    try:
        db.commit()
        return onboard_student
    except SQLAlchemyError as e:
        if "duplicate key value violates unique constraint" in str(e):
            raise HTTPException(
                status_code=404, detail="Registry id already exits")
    finally:
        # Close the session
        db.close()

if __name__ == "__main__":
    uvicorn.run("main:app", host='0.0.0.0', port=8000, reload=True)
