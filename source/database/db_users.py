import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = 'db_users.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = 'users'


# Criar tabela caso não exista
def init_db():
    connection_ = sqlite3.connect(DB_FILE)
    cursor_ = connection_.cursor()
    cursor_.execute(
        f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
        '(id INTEGER PRIMARY KEY AUTOINCREMENT,'
        'nome TEXT,'
        'data_nascimento TEXT,'
        'score INTEGER)'
    )
    connection_.commit()
    connection_.close()


class SQLiteMiddleware:
    def __init__(self, app):
        self.app = app

    async def __call__(self, scope, receive, send):
        if scope["type"] == "http":
            connection_ = sqlite3.connect(DB_FILE)
            cursor_ = connection_.cursor()
            scope["sqlite_connection"] = connection_
            scope["sqlite_cursor"] = cursor_
        await self.app(scope, receive, send)
        if scope["type"] == "http":
            connection_ = scope.pop("sqlite_connection")
            cursor_ = scope.pop("sqlite_cursor")
            cursor_.close()
            connection_.close()