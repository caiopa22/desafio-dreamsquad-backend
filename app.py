from dotenv import load_dotenv
from fastapi import FastAPI
from routers import chat
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Desafio DreamSquad", version=1.0)

origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chat.chat_router)


@app.get("/health")
def getHealth():
    return {"status": "ok"}