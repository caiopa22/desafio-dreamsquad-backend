import os
from dotenv import load_dotenv
import requests
from fastapi import APIRouter, HTTPException
from models.chat import ChatRequest, ChatResponse
from agent import agent as agent_model

chat_router = APIRouter(prefix="/chat", tags=["chat"])

agent = agent_model

@chat_router.post("/")
async def chat(payload: ChatRequest):
    response = agent(payload.message)
    return {"response": response.message}

@chat_router.post("/reset")
async def reset_context():
    try:
        agent.messages = []
        return {"status": "ok", "message": "Contexto do agente resetado com sucesso."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))