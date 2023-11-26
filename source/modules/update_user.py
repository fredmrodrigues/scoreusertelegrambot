from telegram import Update
from telegram.ext import CallbackContext, ConversationHandler
from database.db_users import sqlite3, init_db, DB_FILE, TABLE_NAME

# Estados da conversa
ID_INPUT, EDIT_NOME, EDIT_DATA_NASCIMENTO, EDIT_SCORE, CONFIRM_EDIT = range(5)

async def update_(update: Update, context: CallbackContext):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Editar usuário:")
    await update.message.reply_text("Digite o ID do usuário que deseja editar:")
    return ID_INPUT

async def get_user_id_for_update(update: Update, context: CallbackContext):
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
        await update.message.reply_text(f'Informações do usuário a ser editado (ID: {user_id}):\n'
                                        f'Nome: {user_data[1]}\n'
                                        f'Data de Nascimento: {user_data[2]}\n'
                                        f'Score: {user_data[3]}')
        context.user_data['user_id'] = user_id
        await update.message.reply_text('Digite o novo nome do usuário:')
        return EDIT_NOME
    except ValueError:
        await update.message.reply_text("ID deve ser um número inteiro")
        await update.message.reply_text("Digite o ID do usuário que deseja editar:")
        return ID_INPUT
    except Exception as e:
        await update.message.reply_text(f"Erro ao obter informações do usuário: {str(e)}")
        return ConversationHandler.END
    
async def edit_nome(update: Update, context: CallbackContext):
    novo_nome = update.message.text
    context.user_data['novo_nome'] = novo_nome
    await update.message.reply_text('Digite a nova data de nascimento do usuário:')
    return EDIT_DATA_NASCIMENTO

async def edit_data_nascimento(update: Update, context: CallbackContext):
    nova_data_nascimento = update.message.text
    context.user_data['nova_data_nascimento'] = nova_data_nascimento
    await update.message.reply_text('Digite o novo score do usuário:')
    return EDIT_SCORE

async def edit_score(update: Update, context: CallbackContext):
    novo_score_text = update.message.text
    try:
        novo_score = int(novo_score_text)
        context.user_data['novo_score'] = novo_score
        await update.message.reply_text('Deseja realmente editar este usuário? Responda "sim" ou "não".')
        return CONFIRM_EDIT
    except ValueError:
        await update.message.reply_text("Score deve ser um número inteiro")
        await update.message.reply_text('Digite o novo score do usuário:')
        return EDIT_SCORE

async def ask_for_confirm_edit(update: Update, context: CallbackContext):
    confirm = update.message.text.lower()
    if confirm == "sim":
        try:
            init_db()
            connection_ = sqlite3.connect(DB_FILE)
            cursor_ = connection_.cursor()
            user_id = context.user_data['user_id']
            novo_nome = context.user_data['novo_nome']
            nova_data_nascimento = context.user_data['nova_data_nascimento']
            novo_score = context.user_data['novo_score']
            cursor_.execute(
                f'UPDATE {TABLE_NAME} SET '
                'nome=?, data_nascimento=?, score=? WHERE id=?',
                (novo_nome, nova_data_nascimento, novo_score, user_id)
            )
            connection_.commit()
            cursor_.close()
            connection_.close()
            await update.message.reply_text(f'Usuário com ID {user_id} editado com sucesso!')
        except Exception as e:
            await update.message.reply_text(f"Erro ao editar usuário: {str(e)}")
    else:
        await update.message.reply_text('Operação de edição cancelada.')
    return START