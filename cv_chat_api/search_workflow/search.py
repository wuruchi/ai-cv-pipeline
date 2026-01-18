import faiss
from typing import List
from sentence_transformers import SentenceTransformer

EMBED_MODEL_NAME = "all-MiniLM-L6-v2"
class SearchSimilar:
    def __init__(
            self,
            base_index,
            all_chunk_text: List[str],
            all_metadata: List[dict],
            embed_model_name = EMBED_MODEL_NAME
        ):
        """
        Initializes the SearchSimilar instance.
        Args:
            base_index: The FAISS index containing known embeddings.
            all_chunk_text (List[str]): List of all text chunks.
            all_metadata (List[dict]): List of metadata corresponding to each text chunk.
            embed_model_name (str): The name of the embedding model to use.
        """
        self.embed_model = SentenceTransformer(embed_model_name)
        self.faiss_index = base_index
        self.all_chunk_text = all_chunk_text
        self.all_metadata = all_metadata

    def search(self, question: str, top_k: int = 8):
        """
        Searches for the top_k most similar embeddings to the question.
        Args:
            question (str): The input question to search for.
            top_k (int): The number of top similar results to return.
        Returns:
            List[dict]: A list of dictionaries containing chunk_text and metadata for the top_k similar results.
        """
        question_embedding = self.embed_model.encode([question], convert_to_numpy=True)
        faiss.normalize_L2(question_embedding)
        _, indices = self.faiss_index.search(question_embedding, top_k)
        results = []
        for idx in indices[0]:
            chunk_text = self.all_chunk_text[idx]
            metadata = self.all_metadata[idx]
            results.append({"chunk_text": chunk_text, **metadata})
        return results