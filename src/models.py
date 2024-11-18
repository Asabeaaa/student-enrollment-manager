from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime, date
from sqlalchemy import String, DateTime, Date
from sqlalchemy.sql import func


class Base(DeclarativeBase):
    pass


class Registry(Base):
    __tablename__ = "registry"

    registryId: Mapped[UUID] = mapped_column(UUID, primary_key=True)
    studentId: Mapped[UUID] = mapped_column(UUID, nullable=False)
    classId: Mapped[UUID] = mapped_column(UUID, nullable=False)
    status: Mapped[str] = mapped_column(String, nullable=False)
    dateCreated: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), nullable=False)
    lastUpdated: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now())


class Class(Base):
    __tablename__ = "classes"

    classId: Mapped[UUID] = mapped_column(UUID, primary_key=True)
    level: Mapped[str] = mapped_column(String, nullable=False)
    name: Mapped[str] = mapped_column(String, nullable=False)
    dateCreated: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), nullable=False)
    lastUpdated: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now())


class Course(Base):
    __tablename__ = "courses"

    courseId: Mapped[UUID] = mapped_column(UUID, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    dateCreated: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), nullable=False)
    lastUpdated: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now())


class Student(Base):
    __tablename__ = "students"

    studentId: Mapped[UUID] = mapped_column(UUID, primary_key=True)
    firstName: Mapped[str] = mapped_column(String, nullable=False)
    otherNames: Mapped[str] = mapped_column(String, nullable=True)
    lastName: Mapped[str] = mapped_column(String, nullable=False)
    dateOfBirth: Mapped[date] = mapped_column(Date, nullable=False)


class StudentCourse(Base):
    __tablename__ = "student_courses"

    studentCoursesId: Mapped[UUID] = mapped_column(UUID, primary_key=True)
    studentId: Mapped[UUID] = mapped_column(UUID, nullable=False)
    courseId: Mapped[UUID] = mapped_column(UUID, nullable=False)
    status: Mapped[str] = mapped_column(String, nullable=False)
    dateCreated: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), nullable=False)
    lastUpdated: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now())
