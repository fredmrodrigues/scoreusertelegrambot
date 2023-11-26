# SCOREUSER TELEGRAM BOT
Aplicação de teste
Teste proposto por Daniel @Folzeck

## Enunciado
Você deve fazer uma aplicação distribuída:

Deve utilizar Python 3.11 

Deve fazer uma API utilizando a biblioteca FastAPI que faça um CRUD de usuários 

O usuário deve conter:
Nome, data de nascimento, score (Serasa)

Além do CRUD, deve ter uma, rota que me retorne os usuários que tem um score maior que X (esse valor deve ser recebido por query parameter), caso eu não envie esse valor, deve me retornar os 50 maiores scores 


Depois de finalizado a API, fazer um botzinho muito simples no telegram, pra fazer a conversação e fazer as chamadas pela API através dele

### Bibliotecas / Frameworks externas:
* Python Telegram Bot
    > Version: 20.6
    > Home-page: https://python-telegram-bot.org/
    > License: LGPLv3

* FastAPI (Version: 0.104.1)
    > Version: 0.104.1
    > Home-page: https://fastapi.tiangolo.com/
    > License: MIT license

* Uvicorn (Version: 0.24.0.post1)
    > Version: 0.24.0.post1
    > Home-page: https://www.uvicorn.org/
    > License: BSD 3-Clause "New" or "Revised" License

### Base de dados:
* SQLite3

### FastAPI:
[FastAPI](/docs/FASTAPI.md)

### Telegram Bot:
[Telegram_Bot](/docs/TELEGRAMBOT.md)