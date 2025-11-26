from dotenv import load_dotenv
from fastapi import FastAPI
from routers import chat

app = FastAPI(title="Desafio DreamSquad", version=1.0)
app.include_router(chat.chat_router)

@app.get("/health")
def getHealth():
    return {"status": "ok"}