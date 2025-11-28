from pydantic import BaseModel

# Definição dos modelos que o chat precisa

class ChatRequest(BaseModel):
    message: str
    
class ChatResponse(BaseModel):
    response: str
