from sqlalchemy import String, DateTime, Date
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, UUID

Base = declarative_base()


class Registry(Base):
    __tablename__ = "registry"

    registryId = Column(UUID, primary_key=True, index=True)
    studentId = Column(UUID, nullable=False)
    classId = Column(UUID, nullable=False)
    status = Column(String, nullable=False, index=True)
    dateCreated = Column(DateTime(timezone=True),
                         nullable=False, server_default=func.now())
    lastUpdated = Column(DateTime(timezone=True),
                         nullable=False, server_default=func.now())


class Class(Base):
    __tablename__ = "classes"

    classId = Column(UUID, primary_key=True, index=True)
    level = Column(String, nullable=False, index=True)
    name = Column(String, nullable=False, index=True)
    dateCreated = Column(DateTime(timezone=True),
                         nullable=False, server_default=func.now())
    lastUpdated = Column(DateTime(timezone=True),
                         nullable=False, server_default=func.now())


class Course(Base):
    __tablename__ = "courses"

    courseId = Column(UUID, primary_key=True, index=True)
    name = Column(String, nullable=False, index=True)
    dateCreated = Column(DateTime(timezone=True),
                         nullable=False, server_default=func.now())
    lastUpdated = Column(DateTime(timezone=True),
                         nullable=False, server_default=func.now())


class Student(Base):
    __tablename__ = "students"

    studentId = Column(UUID, primary_key=True, index=True)
    firstName = Column(String, nullable=False)
    otherNames = Column(String, nullable=True)
    lastName = Column(String, nullable=False)
    dateOfBirth = Column(Date, nullable=False)


class StudentCourse(Base):
    __tablename__ = "student_courses"

    studentCoursesId = Column(UUID, primary_key=True, index=True)
    studentId = Column(UUID, nullable=False)
    courseId = Column(UUID, nullable=False)
    status = Column(String, nullable=False, index=True)
    dateCreated = Column(DateTime(timezone=True),
                         nullable=False, server_default=func.now())
    lastUpdated = Column(DateTime(timezone=True),
                         nullable=False, server_default=func.now())
