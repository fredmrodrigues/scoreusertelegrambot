from telegram import Update
from telegram.ext import ConversationHandler, CallbackContext
from database.db_users import sqlite3, init_db, DB_FILE, TABLE_NAME

# Estados da conversa
SCORE_OPTION, SCORE_INPUT = range(2)

async def read_(update: Update, context: CallbackContext):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Filtrar usuários por score:")
    await update.message.reply_text("Deseja informar um valor para score? responda 's' para sim ou 'n' para não.")
    return SCORE_OPTION

async def ask_for_score_option(update: Update, context: CallbackContext):
    user_id = update.message.from_user.id
    score_option = update.message.text.lower()
    if score_option == 's':
        await update.message.reply_text("Digite o valor para score:")
        return SCORE_INPUT
    elif score_option == 'n':
        await show_top_users(update, context)
        return ConversationHandler.END
    else:
        await update.message.reply_text("resposta inválida. Responda 's' para sim ou 'n' para não.")
        return SCORE_OPTION
    
async def get_user_score(update: Update, context: CallbackContext):
    user_id = update.message.from_user.id
    score_text = update.message.text

    try:
        init_db()
        connection_ = sqlite3.connect(DB_FILE)
        cursor_ = connection_.cursor()
        if score_text.isdigit():
            X = int(score_text)
            cursor_.execute(
                f'SELECT * FROM {TABLE_NAME} WHERE score >= ? ORDER BY score DESC', (X,)
            )
            users_data = cursor_.fetchall()
            if not users_data:
                await update.message.reply_text(f"Nenhum usuário encontrado com score maior ou igual a {X}")
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
                await update.message.reply_text(f"Usuários com score maior ou igual a {X}: {users_list}")
        else:
            await update.message.reply_text("Por favor, digite um valor válido para o score (inteiro).")
    except Exception as e:
        await update.message.reply_text(f"Erro ao obter usuários por score: {str(e)}")
    return ConversationHandler.END

async def show_top_users(update: Update, context: CallbackContext):
    try:
        connection_ = sqlite3.connect(DB_FILE)
        cursor_ = connection_.cursor()

        cursor_.execute(
            f'SELECT * FROM {TABLE_NAME} ORDER BY score DESC LIMIT 50'
        )
        users_data = cursor_.fetchall()
        if not users_data:
            await update.message.reply_text("Nenhum usuário encontrado.")
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
            await update.message.reply_text(f"Os 50 usuários com maiores scores: {users_list}")
    except Exception as e:
        await update.message.reply_text(f"Erro ao obter usuários: {str(e)}")
    return ConversationHandler.END