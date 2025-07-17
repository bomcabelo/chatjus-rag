import os
import numpy as np
from openai import OpenAI
from elasticsearch import Elasticsearch
from langchain.chat_models import ChatOpenAI
from langchain.schema import Document
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

llm = ChatOpenAI(temperature=0.2, model="gpt-4", openai_api_key=OPENAI_API_KEY)
es = Elasticsearch("http://localhost:9200")

def buscar_documentos(pergunta, top_k=3):
    from sentence_transformers import SentenceTransformer
    model = SentenceTransformer("sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2")
    query_vector = model.encode(pergunta).tolist()

    response = es.search(index="eproc-decisoes", body={
        "size": top_k,
        "query": {
            "script_score": {
                "query": {"match_all": {}},
                "script": {
                    "source": "cosineSimilarity(params.query_vector, 'embedding') + 1.0",
                    "params": {"query_vector": query_vector}
                }
            }
        }
    })

    documentos = []
    for hit in response["hits"]["hits"]:
        documentos.append(Document(
            page_content=hit["_source"]["conteudo"],
            metadata={"processo": hit["_source"]["numero_processo"]}
        ))
    return documentos

def responder_pergunta(pergunta):
    docs = buscar_documentos(pergunta)
    context = "\n\n".join([doc.page_content for doc in docs])

    prompt = f"""Você é um assistente jurídico especializado em decisões do eProc.

Baseado nas decisões a seguir:

{context}

Responda à seguinte pergunta de forma objetiva e fundamentada:

{pergunta}
"""
    resposta = llm.predict(prompt)
    return resposta, docs
