from strands import tool
from models.tool import MathInput
import json
from typing import Union


@tool
def MathTool(data: Union[MathInput, dict, str]) -> str:
    """
    USAR APENAS para cálculos matemáticos explícitos como:
    - Operações aritméticas: 2+2, 10*5, 100/4
    - Expressões algébricas: x**2, sqrt(16)
    - Porcentagens: 20% de 100
    
    NÃO USAR para:
    - Perguntas gerais
    - Conversas
    - Eventos históricos
    - Qualquer coisa que não seja matemática
    
    Args:
        data: Expressão matemática como string, dict ou MathInput
    """

    # Normaliza o input em um dict
    try:
        if isinstance(data, MathInput):
            parsed = data.model_dump()

        elif isinstance(data, dict):
            parsed = data

        elif isinstance(data, str):
            try:
                parsed = json.loads(data)  # string JSON
            except json.JSONDecodeError:
                parsed = {"query": data}   # string pura "2+2"
        else:
            return "MathTool: tipo de entrada inválido."

        # Extrai query (aceita vários formatos)
        query = (
            parsed.get("query")
            or parsed.get("q")
            or parsed.get("data", {}).get("query")
            or parsed.get("data", {}).get("q")
        )

        if not query:
            return "MathTool: query não encontrada."

        # Eval seguro
        result = eval(query, {"__builtins__": None}, {})
        return str(result)

    except Exception:
        return "Não consegui resolver a operação."
