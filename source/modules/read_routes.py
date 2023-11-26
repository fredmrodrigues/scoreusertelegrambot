from typing import Optional
from fastapi import APIRouter
from database.db_users import sqlite3, DB_FILE, TABLE_NAME

router = APIRouter()

# Rota para obter usuários por score
@router.get("/get_users_by_score")
def get_users_by_score_route(X: Optional[int] = None):
    try:
        connection_ = sqlite3.connect(DB_FILE)
        cursor_ = connection_.cursor()
        if X is None:  # se não for fornecido um valor para X
            cursor_.execute(
                f'SELECT * FROM {TABLE_NAME} ORDER BY score DESC LIMIT 50'
            )
            users_data = cursor_.fetchall()

            if not users_data:
                return {"message": 'Nenhum usuário encontrado.'}
            else:
                users_list = []
                for user_data in users_data:
                    user_info = {
                        "id": user_data[0],
                        "nome": user_data[1],
                        "data_nascimento": user_data[2],
                        "score": user_data[3]
                    }
                    users_list.append(user_info)

                return {"message": "Os 50 usuários com maiores scores:", "users": users_list}
            
        else:
            cursor_.execute(
                f'SELECT * FROM {TABLE_NAME} WHERE score > ? ORDER BY score DESC', (X,)
            )
            users_data = cursor_.fetchall()

            if not users_data:
                return {"message": f"Nenhum usuário encontrado com score maior que {X}."}
            else:
                users_list = []
                for user_data in users_data:
                    user_info = {
                        "id": user_data[0],
                        "nome": user_data[1],
                        "data_nascimento": user_data[2],
                        "score": user_data[3]
                    }
                    users_list.append(user_info)

                return {"message": f'Usuários com score maior que {X}:', "users": users_list}

    except Exception as e:
        return {"error": f"Erro ao obter usuários por score: {str(e)}"}