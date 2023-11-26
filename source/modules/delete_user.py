from telegram import Update
from telegram.ext import CallbackContext, ConversationHandler
from database.db_users import sqlite3, init_db, DB_FILE, TABLE_NAME

# Estados da conversa
ID_INPUT, CONFIRM_DELETE = range(2)

async def delete_(update: Update, context: CallbackContext):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Excluir usuário:")
    await update.message.reply_text("Digite o ID do usuário que deseja excluir:")
    return ID_INPUT

async def get_user_id(update: Update, context: CallbackContext):
    user_id_text = update.message.text
    try:
        user_id = int(user_id_text)
        init_db()
        connection_ = sqlite3.connect(DB_FILE)
        cursor_ = connection_.cursor()
        cursor_.execute(
            f'SELECT * FROM {TABLE_NAME} WHERE id = ?',
            (user_id,)
        )
        user_data = cursor_.fetchone()
        if not user_data:
            await update.message.reply_text(f'Usuário com ID {user_id} não encontrado.')
            return ConversationHandler.END
        await update.message.reply_text(f'Informações do usuário a ser excluído (ID: {user_id}):\n'
                                        f'Nome: {user_data[1]}\n'
                                        f'Data de Nascimento: {user_data[2]}\n'
                                        f'Score: {user_data[3]}')
        context.user_data['user_id'] = user_id
        await update.message.reply_text('Deseja realmente excluir este usuário? Responda "sim" ou "não".')
        return CONFIRM_DELETE
    except ValueError:
        await update.message.reply_text("ID deve ser um número inteiro")
        await update.message.reply_text("Digite o ID do usuário que deseja excluir:")
        return ID_INPUT
    except Exception as e:
        await update.message.reply_text(f"Erro ao obter informações do usuário: {str(e)}")
        return ConversationHandler.END

async def ask_for_confirm_delete(update: Update, context: CallbackContext):
    confirm = update.message.text.lower()
    if confirm == "sim":
        try:
            init_db()
            connection_ = sqlite3.connect(DB_FILE)
            cursor_ = connection_.cursor()
            cursor_.execute(
                f'DELETE FROM {TABLE_NAME} WHERE id = ?',
                (context.user_data['user_id'],)
            )
            connection_.commit()
            cursor_.close()
            connection_.close()
            await update.message.reply_text(f'Usuário com ID {context.user_data["user_id"]} excluído com sucesso!')
        except Exception as e:
            await update.message.reply_text(f"Erro ao excluir usuário: {str(e)}")
    else:
        await update.message.reply_text('Operação de exclusão cancelada.')
    return ConversationHandler.END