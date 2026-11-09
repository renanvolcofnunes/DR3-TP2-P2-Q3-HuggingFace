from contextlib import asynccontextmanager
from fastapi import FastAPI
from pydantic import BaseModel, Field
from models import load_translation_model, tradutor

@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.tokenizer, app.state.modelo = load_translation_model()
    yield
    app.state.tokenizer = None
    app.state.modelo = None

app = FastAPI(title="TP2 - Parte 2 - Q3 - HuggingFace", description="API de tradução inglês-alemão utilizando LangChain e HuggingFace.", lifespan=lifespan)

class TranslationRequest(BaseModel):
    text: str = Field(min_length=1)

class TranslationResponse(BaseModel):
    text: str
    translated_text: str

@app.post("/translate", response_model=TranslationResponse)
def translate(request: TranslationRequest):
    dados = {"tokenizer": app.state.tokenizer, "modelo": app.state.modelo, "text": request.text}
    resultado = tradutor.invoke(dados)

    return TranslationResponse(text=request.text, translated_text=resultado)
