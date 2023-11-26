if __name__ == "__main__":
    from database.db_users import init_db
    from modules.app_initializer import initialize_app
    
    app = initialize_app()  # Inicializa o app
    init_db()  # Inicializa o banco de dados

    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)