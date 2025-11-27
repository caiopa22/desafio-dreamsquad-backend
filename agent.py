import os
from dotenv import load_dotenv
from strands import Agent 
from strands.models.ollama import OllamaModel
from tools.calculator import calculator
# from strands_tools import calculator

load_dotenv()

MODEL = os.getenv("LLM_MODEL")
BASE_URL = os.getenv("OLLAMA_BASE_URL")
AGENT_NAME = os.getenv("AGENT_NAME")
TEMPERATURE = os.getenv("TEMPERATURE")

ollama_model = OllamaModel(
    model_id=MODEL,    
    host=BASE_URL,
    streaming=False
)

# System prompt minimalista
agent = Agent(
    name=AGENT_NAME,
    model=ollama_model,
    tools=[calculator],
    system_prompt=(
        f"Você é {AGENT_NAME}, um assistente em português. 2"
        "Use a ferramenta calculator APENAS para cálculos explícitos. "
        "Ao apresentar resultados matemáticos, formate-os de forma clara e direta."
    )
)

