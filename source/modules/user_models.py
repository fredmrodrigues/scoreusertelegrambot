from pydantic import BaseModel

class UserBase(BaseModel):
    nome: str
    data_nascimento: str
    score: int

class UserEdit(UserBase):
    id: int

class UserDelete(UserBase):
    id: int