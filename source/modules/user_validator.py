import re
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, validator

class UserValidator(BaseModel):
    id: Optional[int]
    nome: str
    data_nascimento: str
    score: int

    @validator("id", pre=True, always=True)
    def default_id(cls, value, values):
        return value or None

    @validator("nome")
    def validate_nome(cls, value):
        if not re.match(r"^[A-Za-z ]+$", value):
            raise ValueError('O campo "nome" deve conter apenas letras ou espaço.')
        return value
    
    @validator("data_nascimento")
    def validate_data_nascimento(cls, value):
        try:
            datetime.strptime(value, "%d/%m/%Y")
        except ValueError:
            raise ValueError ('O campo "data_nascimento" deve estar no formato "dd/mm/aaaa" e ser uma data válida.')
        return value
    
    @validator("score")
    def validate_score(cls, value):
        if value < 0 or value > 1000:
            raise ValueError('O campo "score" deve ser um número inteiro entre 0 e 1000.')
        return value