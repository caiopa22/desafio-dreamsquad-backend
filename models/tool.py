from pydantic import BaseModel

class MathInput(BaseModel):
    query: str