from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str

class UserResponse(UserCreate):
    id: int
    
    class Config:
        orm_mode = True
