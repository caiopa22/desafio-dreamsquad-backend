import os
from dotenv import load_dotenv
from strands import Agent 
from strands.models.ollama import OllamaModel
from tools.math_tool import MathTool

load_dotenv()

MODEL = os.getenv("LLM_MODEL")
BASE_URL = os.getenv("OLLAMA_BASE_URL")
AGENT_NAME = os.getenv("AGENT_NAME")

ollama_model = OllamaModel(
    model_id=MODEL,    
    host=BASE_URL,
    streaming=False
)

agent = Agent(
    name=AGENT_NAME,
    model=ollama_model,
    tools=[MathTool],
    system_prompt=(
        f"""Você é {AGENT_NAME}, um assistente conversacional.

        REGRA IMPORTANTE:
        - Use MathTool SOMENTE quando o usuário pedir um CÁLCULO direto
        Exemplos: "quanto é 2+2", "calcule 15% de 200", "raiz de 144"
        
        - Para QUALQUER outra pergunta, responda diretamente SEM usar ferramentas
        Exemplos: "o que aconteceu com X", "quem é Y", "me explique Z", "O que é W"

        Se a pergunta não for um cálculo matemático explícito, converse normalmente.
        """
    )
)