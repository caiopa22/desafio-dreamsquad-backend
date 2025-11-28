from strands import tool
from models.tool import MathInput
import json
from typing import Union


# Ferramenta para realizar cálculos matemáticos

@tool
def calculator(data: Union[MathInput, dict, str]) -> str:
    """
    Calcula expressões matemáticas explícitas.
    Exemplos: "2+2", "10*5", "20% de 100"
    Use SOMENTE quando houver uma operação matemática clara.
    """

    # Normaliza a entrada de dados para manter consistência entre perguntas
    try:
        if isinstance(data, MathInput):
            parsed = data.model_dump()

        elif isinstance(data, dict):
            parsed = data

        elif isinstance(data, str):
            try:
                parsed = json.loads(data)
            except json.JSONDecodeError:
                parsed = {"query": data}
        else:
            return "MathTool: tipo de entrada inválido."

        # Extrai query após formatação
        query = (
            parsed.get("query")
            or parsed.get("q")
            or parsed.get("data", {}).get("query")
            or parsed.get("data", {}).get("q")
        )

        if not query:
            return "MathTool: query não encontrada."

        # Gerando eval com __builtins__ desabilitados
        result = eval(query, {"__builtins__": None}, {})
        return str(result)

    except Exception:
        return "Não consegui resolver a operação."
