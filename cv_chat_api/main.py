import os
import logging
from pathlib import Path
from typing import List, Dict
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv

from search_workflow.search import SearchSimilar
from search_workflow.prompt import build_prompt
from embeddings_workflow.workflow import workflow as embeddings_workflow
from embeddings_workflow.chunk import SimpleChunker

from ai_clients.perplexityai import PerplexityAiClient
from ai_clients.openai import OpenAiClient
from ai_clients.genai import GenAiClient

TOP_RESULTS = 5
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO").upper()
logging.root.setLevel(LOG_LEVEL)
logging.handlers = logging.StreamHandler()
logging.basicConfig(level=LOG_LEVEL, format="%(asctime)s - %(levelname)s - %(message)s")


logging.info("Starting CV Chat API service...")
logging.info(f"Using log level: {LOG_LEVEL}")

load_dotenv()

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


directory = Path(__file__).parent / "data"
all_chunk_text, all_metadata, embeddings, faiss_index, all_ids = embeddings_workflow(directory, chunker=SimpleChunker(800))
search_similar = SearchSimilar(
    base_index=faiss_index,
    all_chunk_text=all_chunk_text,
    all_metadata=all_metadata,
)

class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    reply: str
    sources: List[Dict]

def call_llm(prompt: str) -> str:
    # client = PerplexityAiClient()
    # client = OpenAiClient()
    client = GenAiClient()
    response = client.query(prompt)
    return response

@app.post("/chat", response_model=ChatResponse)
def chat_endpoint(request: ChatRequest):
    logging.info(f"Received chat request: {request.message}")
    contexts = search_similar.search(
        question=request.message,
        top_k=TOP_RESULTS,
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
                    "cvId": ctx['cv_id'],
                    "candidateName": ctx['candidate_name'],
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
