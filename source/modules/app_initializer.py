from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from modules.create_routes import router as create_router
from modules.read_routes import router as read_router
from modules.update_routes import router as update_router
from modules.delete_routes import router as delete_router
from database.db_users import SQLiteMiddleware

def initialize_app():
    app = FastAPI()

    # Configuração de CORS para permitir todas as origens durante o desenvolvimento
    origins = ["*"]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
    )

    # Middleware para criar uma nova conexão e cursor para cada solicitação
    app.add_middleware(SQLiteMiddleware)

    # Importe dos roteadores sem especificar o caminho completo
    app.include_router(create_router, prefix="/create", tags=["create"])
    app.include_router(read_router, prefix="/read", tags=["read"])
    app.include_router(update_router, prefix="/update", tags=["update"])
    app.include_router(delete_router, prefix="/delete", tags=["delete"])
    
    @app.get("/")
    def read_root():
        return {"message":
                "Consulte a documentação para obter os endpoints disponíveis."}
    return app