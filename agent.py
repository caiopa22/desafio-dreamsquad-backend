import os
from dotenv import load_dotenv
from strands import Agent 
from strands.models.ollama import OllamaModel
from tools.calculator import calculator

load_dotenv()

# Puxando dados do .env
MODEL = os.getenv("LLM_MODEL")
BASE_URL = os.getenv("OLLAMA_BASE_URL")
AGENT_NAME = os.getenv("AGENT_NAME")

# Definindo modelo que será utilizado
ollama_model = OllamaModel(
    model_id=MODEL,    
    host=BASE_URL
)

# Criação e configuração do agente
agent = Agent(
    name=AGENT_NAME,
    model=ollama_model,
    tools=[calculator],
    system_prompt=(
        f"Você é {AGENT_NAME}, um assistente em português."
        "Seja gentil, como se estivesse conversando com um amigo."
        "Use a ferramenta calculator APENAS para cálculos explícitos."
        "Ao apresentar resultados matemáticos, formate-os de forma clara e direta, como um amigo faria."
        "Exemplo: 'O resultado de 2 mais 2 é 4'."
        "Evite o uso de formatação técnica como LaTeX."
    )
)