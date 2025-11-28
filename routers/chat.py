import os
from dotenv import load_dotenv
import requests
from fastapi import APIRouter, HTTPException, Body
from models.chat import ChatRequest, ChatResponse
from agent import agent as agent_model

chat_router = APIRouter(prefix="/chat", tags=["Chat"])
agent = agent_model


# Rota principal para engajar com o agente
@chat_router.post(
    "/",
    summary="Conversar com o agente",
    description="Envia uma mensagem para o agente de IA e recebe uma resposta personalizada",
    responses={
        200: {
            "description": "Resposta bem-sucedida do agente",
            "content": {
                "application/json": {
                    "example": {
                        "response": {
                            "role": "assistant",
                            "content": [
                                {
                                    "text": "Olá! Estou aqui para ajudar você com suas dúvidas gerais e cálculos matemáticos!"
                                }
                            ]
                        }
                    }
                }
            }
        }
    }
)
async def chat(payload: ChatRequest):
    """
    Processa uma mensagem do usuário e retorna a resposta do agente de IA.
    """
    try:
        response = agent(payload.message)
        return {"response": response.message}  # ← Mantém como estava
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Rota adicional para resetar o contexto do agente
@chat_router.post(
    "/reset",
    summary="Resetar contexto da conversa",
    description="Limpa todo o histórico de mensagens do agente",
    responses={
        200: {
            "description": "Contexto resetado com sucesso",
            "content": {
                "application/json": {
                    "example": {
                        "status": "ok",
                        "message": "Contexto do agente resetado com sucesso."
                    }
                }
            }
        }
    }
)
async def reset_context():
    """Reseta o contexto do agente"""
    try:
        agent.messages = []
        return {
            "status": "ok",
            "message": "Contexto do agente resetado com sucesso."
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))