from typing import List
from abc import ABC, abstractmethod

MAX_CHARS = 200

class Chunker(ABC):
    """Abstract base class for text chunkers."""

    @abstractmethod
    def chunk(self, text: str) -> List[str]:
        """Splits text into chunks."""
        pass

class SimpleChunker:
    """A simple text chunker that splits text into chunks of a maximum character length."""

    def __init__(self, max_chars: int = MAX_CHARS):
        self.max_chars = max_chars
    def chunk(self, text: str) -> List[str]:
        """Splits text into chunks not exceeding max_chars."""
        words = text.split()
        chunks, current = [], []
        for w in words:
            current.append(w)
            if sum(len(x) + 1 for x in current) > self.max_chars:
                chunks.append(" ".join(current))
                current = []
        if current:
            chunks.append(" ".join(current))
        return chunks