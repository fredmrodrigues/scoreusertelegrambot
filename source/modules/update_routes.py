from fastapi import APIRouter, HTTPException
from modules.user_validator import UserValidator
from database.db_users import sqlite3, DB_FILE, TABLE_NAME

router = APIRouter()

# Rota para editar um usuário
@router.put("/edit_user")
def edit_user_route(user_edit: UserValidator):
    try:
        connection_ = sqlite3.connect(DB_FILE)
        cursor_ = connection_.cursor()
        # Verificar se o ID existe no banco de dados
        cursor_.execute(
            f'SELECT * FROM {TABLE_NAME} WHERE id = ?',
            (user_edit.id,)
        )
        user_data = cursor_.fetchone()

        if not user_data:
            raise HTTPException(
                status_code=404,
                detail=f'Usuário com ID {user_edit.id} não encontrado.')
        
        # Atualizar as informações no banco de dados
        cursor_.execute(
            f'UPDATE {TABLE_NAME} SET '
            'nome=?, data_nascimento=?, score=? WHERE id=?',
            (user_edit.nome,
             user_edit.data_nascimento,
             user_edit.score,
             user_edit.id)
        )
        connection_.commit()
        return {"message": f'Usuário com ID {user_edit.id} editado com sucesso!'}
    
    except Exception as e:
        return {"error": f"Erro ao editar usuário: {str(e)}"}