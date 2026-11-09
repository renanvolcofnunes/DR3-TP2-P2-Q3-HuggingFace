# Parte 2 - Q3 - Hugging Face

## Descricao
API de traducao do ingles para o alemao com LangChain e Hugging Face.

## Requisitos
Python 3.14 e dependencias listadas em requirements.txt.

## Instalacao
    python -m venv venv
    .\venv\Scripts\Activate.ps1
    python -m pip install -r requirements.txt

## Execucao
    python -m uvicorn main:app --reload --port 8004

## Documentacao da API
http://127.0.0.1:8004/docs

## Endpoint
POST /translate

## Exemplo de requisicao
    {"text":"Hello, how are you today?"}

## Observacoes
Modelo Helsinki-NLP/opus-mt-en-de executado localmente.
