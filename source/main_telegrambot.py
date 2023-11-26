import os
import logging
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, ConversationHandler, MessageHandler, filters
from modules.create_user import *
from modules.read_users import *
from modules.delete_user import *
from modules.update_user import *


load_dotenv()
TOKEN = os.getenv("BOT_KEY")

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="""Bem-vindo ao ScoreUser Telegram Bot!
Clique em um comando:
/create: Criar um novo usuário;
/read: Filtrar usuários por score;
/update: Editar um usuário;
/delete: Deletar um usuário;""")

async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Desculpe, *não* reconheço esse comando.")
 
if __name__ == '__main__':   
    application = ApplicationBuilder().token(TOKEN).build()

    start_handler = CommandHandler('start', start)

    create_handler = ConversationHandler(
        entry_points=[CommandHandler('create', create_)],
        states={
            NOME: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_name)],
            DATA_NASCIMENTO: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_data_nascimento)],
            SCORE: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_score)],
            SUCCESS: [MessageHandler(filters.TEXT & ~filters.COMMAND, success_create)],
        },
        fallbacks=[CommandHandler('cancel', cancel)]
    )

    read_handler = ConversationHandler(
        entry_points=[CommandHandler('read', read_)],
        states={
            SCORE_OPTION: [MessageHandler(filters.TEXT & ~filters.COMMAND, ask_for_score_option)],
            SCORE_INPUT: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_user_score)],
        },
        fallbacks=[CommandHandler('cancel', cancel)]
    )

    update_handler = ConversationHandler(
        entry_points=[CommandHandler('update', update_)],
        states={
            ID_INPUT: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_user_id_for_update)],
            EDIT_NOME: [MessageHandler(filters.TEXT & ~filters.COMMAND, edit_nome)],
            EDIT_DATA_NASCIMENTO: [MessageHandler(filters.TEXT & ~filters.COMMAND, edit_data_nascimento)],
            EDIT_SCORE: [MessageHandler(filters.TEXT & ~filters.COMMAND, edit_score)],
            CONFIRM_EDIT: [MessageHandler(filters.TEXT & ~filters.COMMAND, ask_for_confirm_edit)],
        },
        fallbacks=[CommandHandler('cancel', cancel)]
    )

    delete_handler = ConversationHandler(
        entry_points=[CommandHandler('delete', delete_)],
        states={
            ID_INPUT: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_user_id)],
            CONFIRM_DELETE: [MessageHandler(filters.TEXT & ~filters.COMMAND, ask_for_confirm_delete)],
        },
        fallbacks=[CommandHandler('cancel', cancel)]
    )

    unknown_handler = MessageHandler(filters.COMMAND, unknown)

    application.add_handler(start_handler)
    application.add_handler(create_handler)
    application.add_handler(read_handler)
    application.add_handler(update_handler)
    application.add_handler(delete_handler)
    application.add_handler(unknown_handler)

    application.run_polling()