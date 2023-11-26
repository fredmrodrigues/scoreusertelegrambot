from fastapi import APIRouter, HTTPException
from modules.user_models import UserDelete
from database.db_users import sqlite3, DB_FILE, TABLE_NAME

router = APIRouter()

# Rota para excluir um usuário
@router.delete("/delete_user")
def delete_user_route(user_delete: UserDelete):
    try:
        connection_ = sqlite3.connect(DB_FILE)
        cursor_ = connection_.cursor()
        # Verificar se o ID existe no banco de daods
        cursor_.execute(
            f'SELECT * FROM {TABLE_NAME} WHERE id = ?',
            (user_delete.id,)
        )
        user_data = cursor_.fetchone()

        if not user_data:
            raise HTTPException(
                status_code=404,
                detail=f'Usuário com ID {user_delete.id} não encontrado.')

        # Exibir informações do usuário a ser excluído
        print(f'Informações do usuário a ser excluído (ID: {user_delete.id}):')
        print(f'Nome: {user_data[1]}')
        print(f'Data de Nascimento: {user_data[2]}')
        print(f'Score: {user_data[3]}')

        # Confirmar a exclusão com o usuário
        confirmacao = input('Deseja realmente excluir este usuário? '
                            '(S/N): ').upper()
        
        if confirmacao == 'S':
            # Excluir o usuário do banco de dados
            cursor_.execute(
                f'DELETE FROM {TABLE_NAME} WHERE id=?', (user_delete.id,)
            )
            connection_.commit()

            return {"message": f'Usuário com ID {user_delete.id} excluído com sucesso!'}

        else:
            return {"message": 'Operação de exclusão cancelada.'}

    except Exception as e:
        return {"error": f"Erro ao excluir usuário: {str(e)}"}