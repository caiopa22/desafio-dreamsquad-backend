from dotenv import load_dotenv
from fastapi import FastAPI
from routers import chat
from fastapi.middleware.cors import CORSMiddleware

# Configuração do FastAPI e Swagger
app = FastAPI(
    title="Desafio DreamSquad",
    version="1.0.0",
    description="Uma API de chat desenvolvida como solução para um desafio técnico da Dreamsquad. O backend utiliza um agente de IA que integra modelos LLM locais com ferramentas especializadas para processar mensagens, resolver operações matemáticas e manter contexto de conversação. Tudo executado 100% localmente usando Ollama.",
    docs_url="/docs",
    contact={
        "name": "Caio Pacheco Andrade",
        "email": "caiopacheco060@gmail.com",
    },
)

# URLs permitidas
origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]

# Adicionando Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluindo o roteamento para o chat
app.include_router(chat.chat_router)

# Verificação da API
@app.get(
    "/health",
    tags=["Health"],
    summary="Verificação de saúde da API",
    description="Retorna o status de funcionamento da API",
    responses={
        200: {
            "description": "API está funcionando corretamente",
            "content": {
                "application/json": {
                    "example": {
                        "status": "ok"
                    }
                }
            }
        }
    }
)
def getHealth():
    """
    Endpoint para verificar se a API está funcionando corretamente.
    
    Returns:
        dict: Status da API
    """
    return {"status": "ok"}