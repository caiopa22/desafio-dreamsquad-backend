# ⭐ Desafio - Dreamsquad (Backend)

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-green?logo=fastapi&logoColor=white)
![Ollama](https://img.shields.io/badge/Ollama-Local%20LLM-orange)
![License](https://img.shields.io/badge/License-Private-red)

## 📖 Sobre o projeto

Uma API de chat robusta desenvolvida como solução para um desafio técnico da **Dreamsquad**. O backend utiliza um agente de IA inteligente que integra modelos LLM locais com ferramentas especializadas para processar mensagens, resolver operações matemáticas e manter contexto de conversação. Tudo executado **100% localmente** usando Ollama.

**Para uma melhor experiência de uso e teste**, recomendo utilizar o [frontend complementar](https://github.com/caiopa22/desafio-dreamsquad-frontend), que oferece uma interface para interagir com o agente de IA.

---

## 🎯 Objetivo

Construir um backend capaz de:
- ✅ Receber mensagens via API REST
- ✅ Processar texto usando um agente de IA com Strands Agents
- ✅ Invocar tools especializadas (ex: cálculos matemáticos) quando necessário
- ✅ Manter contexto de conversação entre mensagens
- ✅ Executar tudo localmente sem dependências externas de IA

---

## 🚀 Tecnologias utilizadas

| Tecnologia | Função |
|---|---|
| **FastAPI** | Framework moderno para APIs Python |
| **Strands Agents** | Criação do agente de IA e ferramentas |
| **Ollama** | Execução local de modelos LLM |
| **Pydantic** | Validação de modelos de dados |
| **Uvicorn** | Servidor ASGI |
| **Python 3.10+** | Linguagem base |

---

## 📁 Estrutura do projeto

```
desafio-dreamsquad-backend/
├── agent.py                    # Configuração do agente e integração Ollama
├── app.py                      # Instância FastAPI e registro de rotas
├── models/                     # Modelos Pydantic
│   ├── chat.py                 # Modelo de requisição e resposta
│   └── tool.py                 # Modelo de ferramentas
├── routers/                    # Definição de rotas
│   └── chat.py                 # Router com endpoints de chat
├── tools/
│   └── calculator.py           # Tool matemática para cálculos
├── .env.example                # Exemplo de variáveis de ambiente
├── requirements.txt            # Dependências do projeto
└── README.md
```

---

## 🧠 Como o agente funciona

O agente é construído com:
- Um modelo LLM local (via Ollama)
- Um system prompt minimalista e eficiente
- A tool matemática `calculator` registrada para operações explícitas

**Fluxo de processamento:**

1. Usuário envia mensagem à API (`POST /chat`)
2. Agente processa o texto:
   - Se detectar operação matemática explícita → invoca a **tool calculator**
   - Caso contrário → responde usando o modelo LLM
3. Resposta final é retornada ao cliente com contexto mantido

**Exemplo de uso:**

```json
POST /chat
{
  "message": "Quanto é 45 * 11?"
}

Resposta:
{
  "response": {
    "role": "assistant",
    "content": [
      {
        "text": "O resultado da multiplicação 45 * 11 é 495."
      }
    ]
  }
}
```

---

## ⚙️ Pré-requisitos

Antes de começar, certifique-se de ter instalado:

- **Python 3.10+** — [Download](https://www.python.org/downloads/)
- **Ollama** — [Download](https://ollama.com/download)
- **Git** — Para clonar o repositório

---

## 📦 Instalação

### 1. Clone o repositório

```bash
git clone https://github.com/caiopa22/desafio-dreamsquad-backend
cd desafio-dreamsquad-backend
```

### 2. Crie e ative um ambiente virtual

```bash
# Linux/Mac
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Configure o Ollama e baixe o modelo

```bash
# Inicie o Ollama (ou certifique-se de que está rodando)
ollama serve

# Em outro terminal, baixe o modelo LLM
ollama pull qwen2.5:7b
```

### 5. Configure as variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto:

```bash
touch .env
```

Edite o arquivo `.env` com suas configurações:

```env
LLM_MODEL=qwen2.5:7b
OLLAMA_BASE_URL=http://localhost:11434
AGENT_NAME=Ares AI
TEMPERATURE=0.2
```

**Variáveis disponíveis:**
- `LLM_MODEL` — Modelo LLM instalado no Ollama (recomendado: qwen2.5:7b)
- `OLLAMA_BASE_URL` — URL base do Ollama (padrão: http://localhost:11434)
- `AGENT_NAME` — Nome do agente de IA
- `TEMPERATURE` — Criatividade das respostas (0.0 = determinístico, 1.0 = criativo)

---

## ▶️ Executando o projeto

### 1. Certifique-se que o Ollama está rodando

```bash
ollama serve
```

### 2. Em outro terminal, inicie o servidor FastAPI

```bash
cd desafio-dreamsquad-backend
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate     # Windows

uvicorn app:app --reload
```

Você verá a saída:

```
INFO:     Uvicorn running on http://127.0.0.1:8000
INFO:     Application startup complete
```

---

## 💬 Endpoints

### `POST /chat/`

Envia uma mensagem ao agente e recebe uma resposta processada.

**Request:**
```json
{
  "message": "Olá! Como você está?"
}
```

**Response:**
```json
{
  "response": {
    "role": "assistant",
    "content": [
      {
        "text": "Olá! Tudo bem, obrigado por perguntar! Como posso ajudá-lo?"
      }
    ]
  }
}
```

---

### `POST /chat/reset`

Reseta o contexto do agente, limpando o histórico de conversação.

**Response:**
```json
{
  "status": "ok",
  "message": "Contexto do agente resetado com sucesso."
}
```

---

## 🧪 Testando a API

### Usando o Postman

1. **Abra o Postman**
2. **Crie uma nova requisição POST**
3. **Use a URL:**
   ```
   http://127.0.0.1:8000/chat
   ```
4. **Em Body → raw → JSON, envie:**
   ```json
   {
     "message": "2 + 2 = ?"
   }
   ```
5. **Clique em Send**
6. **Resposta esperada:**
   ```json
   {
     "response": {
       "role": "assistant",
       "content": [
         {
           "text": "2 + 2 = 4"
         }
       ]
     }
   }
   ```

---

## ⚠️ Solução de problemas

| Problema | Solução |
|---|---|
| **"Connection refused" ao conectar ao Ollama** | Certifique-se de que o Ollama está rodando com `ollama serve` |
| **"Model not found"** | Baixe o modelo com `ollama pull qwen2.5:7b` |
| **Porta 8000 já em uso** | Use `uvicorn app:app --reload --port 8001` |
| **Resposta lenta** | O modelo está sendo carregado. Aguarde alguns segundos |

---

## 📝 Exemplo de fluxo completo

```bash
# Terminal 1: Inicie o Ollama
ollama serve

# Terminal 2: Configure e inicie o servidor
cd desafio-dreamsquad-backend
source venv/bin/activate
uvicorn app:app --reload
```
---

## 🔧 Desenvolvimento

Para adicionar novas tools ao agente:

1. Crie um novo arquivo em `tools/`
2. Defina a função com o decorator apropriado
3. Registre a tool no arquivo `agent.py`

Exemplo:

```python
# tools/custom.py
def minha_ferramenta(entrada: str) -> str:
    """Descrição da ferramenta."""
    return f"Processado: {entrada}"
```

---

## 📄 Licença

Desenvolvido exclusivamente para o processo seletivo da **Dreamsquad**.

Todos os direitos reservados.

---

## 👤 Autor

Desenvolvido por **Caio Pacheco Andrade** como solução para o desafio técnico da Dreamsquad.

---

**Última atualização:** Novembro de 2025



