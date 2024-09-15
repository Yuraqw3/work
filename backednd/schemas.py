from pydantic import BaseModel, EmailStr
Base = BaseModel()

class BaseUser(Base):
    name: str
    email: EmailStr
    
class CreateUser(Base):
    password: str
    
class UserInDB(CreateUser):
    id: int