from typing import List
import faiss
from sentence_transformers import SentenceTransformer

EMBED_MODEL_NAME = "all-MiniLM-L6-v2"
embed_model = SentenceTransformer(EMBED_MODEL_NAME)

def get_embedding(chunk_text: List[str]):
    """Generates embeddings for a list of text chunks."""
    embeddings = embed_model.encode(chunk_text)
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    faiss.normalize_L2(embeddings)
    index.add(embeddings)
    return embeddings, index
