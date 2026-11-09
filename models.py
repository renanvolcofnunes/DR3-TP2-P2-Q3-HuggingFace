import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from langchain_core.runnables import RunnableLambda

def load_translation_model():
    model_name = "Helsinki-NLP/opus-mt-en-de"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    modelo = AutoModelForSeq2SeqLM.from_pretrained(model_name)
    modelo.eval()
    return tokenizer, modelo

def translate_text(dados):
    tokenizer = dados["tokenizer"]
    modelo = dados["modelo"]
    text = dados["text"]
    entradas = tokenizer([text], return_tensors="pt", padding=True, truncation=True)

    with torch.no_grad():
        saida = modelo.generate(**entradas, max_new_tokens=256)
    texto_traduzido = tokenizer.decode(saida[0], skip_special_tokens=True)
    return texto_traduzido

tradutor = RunnableLambda(translate_text)
