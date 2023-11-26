from typing import List
from fastapi import APIRouter
from modules.user_validator import UserValidator
from database.db_users import sqlite3, DB_FILE, TABLE_NAME

router = APIRouter()

# Rota para criar um novo usuário
@router.post("/create_user")
def create_user_route(user: UserValidator):
    try:
        connection_ = sqlite3.connect(DB_FILE)
        cursor_ = connection_.cursor()

        # Inserir novo usuário no banco de dados
        cursor_.execute(
            f'INSERT INTO {TABLE_NAME}'
            '(nome, data_nascimento, score)'
            'VALUES'
            '(?, ?, ?)',
            (user.nome, user.data_nascimento, user.score)
        )
        connection_.commit()
        return {"message": "Usuário cadastrado com sucesso!"}
    
    except Exception as e:
        return {"error": f"Erro ao criar usuário: {str(e)}"}


# Rota para criar vários usuários de uma vez
@router.post("/add_users")
def add_users_route(users: List[UserValidator]):
    try:
        connection_ = sqlite3.connect(DB_FILE)
        cursor_ = connection_.cursor()
        for user in users:
            cursor_.execute(
                f'INSERT INTO {TABLE_NAME} '
                '(nome, data_nascimento, score) VALUES '
                '(?, ?, ?)',
                (user.nome, user.data_nascimento, user.score)
            )
        connection_.commit()
        return {"message": f"{len(users)} usuários adicionados com sucesso!"}
    
    except Exception as e:
        return {"error": f"Erro ao adicionar usuários: {str(e)}"}