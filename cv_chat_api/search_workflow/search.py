import faiss
from typing import List
from sentence_transformers import SentenceTransformer

EMBED_MODEL_NAME = "all-MiniLM-L6-v2"
embed_model = SentenceTransformer(EMBED_MODEL_NAME)

def search_similar(question: str, index,  all_chunk_text: List[str], all_metadata: List[dict], top_k: int = 8,):
    """
    Searches for the top_k most similar embeddings to the question.
    Args:
        question (str): The input question to search for.
        index: The FAISS index containing the embeddings.
        all_chunk_text (List[str]): List of all chunk texts.
        all_metadata (List[dict]): List of metadata corresponding to each chunk.
        top_k (int): The number of top similar results to return.
    Returns:
        tuple: (distances, indices) of the top_k similar embeddings.
    """
    question_embedding = embed_model.encode([question], convert_to_numpy=True)
    faiss.normalize_L2(question_embedding)
    distances, indices = index.search(question_embedding, top_k)
    results = []
    for idx in indices[0]:
        chunk_text = all_chunk_text[idx]
        metadata = all_metadata[idx]
        results.append({"chunk_text": chunk_text, **metadata})
    return results