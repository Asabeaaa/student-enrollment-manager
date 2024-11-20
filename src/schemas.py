from pydantic import BaseModel
from datetime import datetime, date
from uuid import UUID
from enum import Enum
from typing import Optional


class RegistryStatus(str, Enum):
    PENDING = "PRNDING"
    PROCESSING = "PROCESSING"
    REGISTERED = "REGISTERED"
    GRADUATED = "GRADUATED"
    UNREGISTERED = "UNREGISTERED"


class StudentCourseStatus(str, Enum):
    REGISTERED = "REGISTERED"
    COMPLETED = "COMPLETED"
    DROPPED = "DROPPED"


class CourseStatus(str, Enum):
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"


class Registry(BaseModel):
    registry_id: UUID
    student_id: UUID
    class_id: UUID
    status: RegistryStatus
    date_created: datetime
    last_updated: datetime

    class Config:
        from_attributes = True


class RegistryCreate(BaseModel):
    student_id: UUID
    class_id: UUID
    status: RegistryStatus
    date_created: datetime
    last_updated: datetime

    class Config:
        from_attributes = True


class Student(BaseModel):
    student_id: Optional[UUID] = None
    first_name: Optional[str] = None
    other_names: Optional[str] = None
    last_name: Optional[str] = None
    date_of_birth: Optional[date] = None

    class Config:
        from_attributes = True


class StudentCreate(BaseModel):
    first_name: str
    other_names: Optional[str] = None
    last_name: str
    date_of_birth: date

    class Config:
        from_attributes = True


class Class(BaseModel):
    class_id: UUID
    level: str
    name: str
    date_created: datetime
    last_updated: datetime

    class Config:
        from_attributes = True


class Course(BaseModel):
    course_id: UUID
    name: CourseStatus
    date_created: datetime
    last_updated: datetime

    class Config:
        from_attributes = True


class StudentCourse(BaseModel):
    student_courses_id: UUID
    student_id: UUID
    course_id: UUID
    status: StudentCourseStatus
    date_created: datetime
    last_updated: datetime

    class Config:
        from_attributes = True
