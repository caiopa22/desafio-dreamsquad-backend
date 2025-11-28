from pydantic import BaseModel, Field

# Definição dos modelos que o chat precisa
class ChatRequest(BaseModel):
    message: str = Field(
        description="Mensagem enviada pelo usuário",
        examples=["Olá! Como você pode me ajudar?"]
    )

    
class ChatResponse(BaseModel):
    response: str = Field(
        description="Resposta do agente",
        examples=["Olá! Estou aqui para ajudar."]
    )