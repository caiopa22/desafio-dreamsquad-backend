import os
from dotenv import load_dotenv
import requests
from fastapi import APIRouter, HTTPException
from models.chat import ChatRequest, ChatResponse
from agent import agent

chat_router = APIRouter(prefix="/chat", tags=["chat"])

@chat_router.post("/")
async def chat(payload: ChatRequest):
    response = agent(payload.message)
    return {"response": response.message}