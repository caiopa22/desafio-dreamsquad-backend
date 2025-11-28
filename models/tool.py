from pydantic import BaseModel

# Definição dos modelos que a Tool usa

class MathInput(BaseModel):
    query: str