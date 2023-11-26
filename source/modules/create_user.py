from telegram import Update
from telegram.ext import ConversationHandler, CallbackContext
from modules.user_validator import UserValidator
from database.db_users import sqlite3, init_db, DB_FILE, TABLE_NAME

user_data = {}

# Estados da conversa
CREATE, NOME, DATA_NASCIMENTO, SCORE, SUCCESS = range(5)

async def create_(update: Update, context: CallbackContext):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Criar usuário:")
    user_id = update.message.from_user.id
    user_data[user_id] = {'id': 0, 'nome': None, 'data_nascimento': None, 'score': 0}
    await update.message.reply_text("Digite o nome do novo usuário:")
    return NOME

async def get_name(update: Update, context: CallbackContext):
    user_id = update.message.from_user.id
    user_data[user_id]['nome'] = update.message.text
    await update.message.reply_text("Digite a data de nascimento do novo usuário:")
    return DATA_NASCIMENTO

async def get_data_nascimento(update: Update, context: CallbackContext):
    user_id = update.message.from_user.id
    user_data[user_id]['data_nascimento'] = update.message.text
    await update.message.reply_text("Digite o score do novo usuário:")
    return SCORE

async def get_score(update: Update, context: CallbackContext):
    user_id = update.message.from_user.id
    score_text = update.message.text
    try:
        user_data[user_id]['score'] = int(score_text)
        if await validate_user_data(user_data[user_id]):
            await update.effective_message.reply_text("Salvando dados...")
            await success_create(update, context)
            return ConversationHandler.END
        else:
            await context.bot.send_message(chat_id=update.effective_chat.id, text="Dados inválidos. Tente novamente.")
            await update.message.reply_text("Digite o nome do novo usuário:")
            return NOME
    except ValueError:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="O score do novo usuário deve ser um número inteiro.")
        await update.message.reply_text("Digite o score do novo usuário:")
        return SCORE

async def validate_user_data(user_data):
    try:
        UserValidator(**user_data)
        return True
    except ValueError as e:
        print(f'Erro de validação: {str(e)}')
        return False

async def success_create(update: Update, context: CallbackContext):
    user_id = update.message.from_user.id
    if await validate_user_data(user_data[user_id]):
        user_data_dict = UserValidator(**user_data[user_id]).dict()
        init_db()
        connection_ = sqlite3.connect(DB_FILE)
        cursor_ = connection_.cursor()
        cursor_.execute(
            f'INSERT INTO {TABLE_NAME}'
            '(nome, data_nascimento, score)'
            'VALUES'
            '(?, ?, ?)',
            (user_data_dict['nome'], user_data_dict['data_nascimento'], user_data_dict['score'])
        )
        connection_.commit()
        connection_.close()
        await update.message.reply_text(f"Novo usuário registrado. {user_data[user_id]}.")
        return ConversationHandler.END
    else:
        await update.message.reply_text("Erro de validação. Não foi possível cadastrar o usuário.")
        return ConversationHandler.END