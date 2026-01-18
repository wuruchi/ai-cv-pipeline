import os
import logging
from typing import List, Dict
from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel
from dotenv import load_dotenv

from search_workflow.search import search_similar
from search_workflow.prompt import build_prompt
from embeddings_workflow.workflow import workflow as embeddings_workflow
from embeddings_workflow.chunk import SimpleChunker

from ai_clients.perplexityai import PerplexityAiClient

LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO").upper()
logging.root.setLevel(LOG_LEVEL)
logging.handlers = logging.StreamHandler()
logging.basicConfig(level=LOG_LEVEL, format="%(asctime)s - %(levelname)s - %(message)s")

load_dotenv()

app = FastAPI()
from pathlib import Path
directory = Path(__file__).parent / "data"
all_chunk_text, all_metadata, embeddings, index, all_ids = embeddings_workflow(directory, chunker=SimpleChunker(300))

class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    reply: str
    sources: List[Dict]

def call_llm(prompt: str) -> str:
    client = PerplexityAiClient()
    response = client.query(prompt)
    return response

@app.post("/chat", response_model=ChatResponse)
def chat_endpoint(request: ChatRequest):
    logging.info(f"Received chat request: {request.message}")
    contexts = search_similar(
        question=request.message,
        index=index,
        all_chunk_text=all_chunk_text,
        all_metadata=all_metadata,
        top_k=5,
    )
    prompt = build_prompt(request.message, contexts)
    reply = call_llm(prompt)
    seen = set()
    unique_sources = []
    for ctx in contexts:
        key = (ctx['cv_id'], ctx['candidate_name'])
        if key not in seen:
            seen.add(key)
            unique_sources.append(
                {
                    "cv_id": ctx['cv_id'],
                    "candidate_name": ctx['candidate_name'],
                }
            )
    logging.info(f"Generated reply: {reply}")
    return ChatResponse(reply=reply, sources=unique_sources)

@app.get("/source/{cv_base_name}")
def get_source(cv_base_name: str):
    full_path = os.path.join(directory, cv_base_name)
    logging
    is_pdf = full_path.lower().endswith(".pdf")
    if not is_pdf:
        return {"error": "Only PDF files are supported"}
    if not os.path.isfile(full_path):
        return {"error": "File not found"}
    return FileResponse(full_path, media_type="application/pdf", filename=cv_base_name)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
