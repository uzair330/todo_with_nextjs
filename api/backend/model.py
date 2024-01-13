from pydantic import BaseModel, Field, EmailStr


from sqlalchemy.orm import declarative_base, Mapped, column_property, relationship
from sqlalchemy import Column, Integer, String, ForeignKey
from .database import Session, engine

Base = declarative_base()


# Creating todos table
class Todo_Table(Base):
    __tablename__ = "todo"
    id = Column(Integer, primary_key=True)
    task = Column(String, nullable=False)
    status = Column(String, nullable=False)

    def __repr__(self):
        return f"<Todo_Table {self.task}>"


# Todo table schema
class TodoSchema(BaseModel):
    task: str = Field(default=None)
    status: str = Field(default=None)

    class config:
        schema_extra = {
            "example": {
                "task": "Do the dishes",
                "status": "In Progress",
            }
        }


def Creating_table():
    Base.metadata.create_all(bind=engine)
    print("Table created")


# Creating Users table
class Users(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    fullname = Column(String, nullable=False)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)

    def __repr__(self):
        return f"<Users {self.fullname}>"


# User Schema
class UserSchema(BaseModel):
    fullname: str = Field(default=None)
    email: EmailStr = Field(default=None)
    password: str = Field(default=None)

    class config:
        schema_extra = {
            "example": {
                "fullname": "John Doe",
                "email": "john@example.com",
                "password": "XXXXXX",
            }
        }


# login schema
class UserLoginSchema(BaseModel):
    email: EmailStr = Field(default=None)
    password: str = Field(default=None)

    class config:
        schema_extra = {
            "example": {
                "email": "john@example.com",
                "password": "XXXXXX",
            }
        }
