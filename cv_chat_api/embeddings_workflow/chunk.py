from typing import List

MAX_CHARS = 100

def simple_chunk(text: str, max_chars: int = MAX_CHARS) -> List[str]:
    """Splits text into chunks not exceeding max_chars."""
    words = text.split()
    chunks, current = [], []
    for w in words:
        current.append(w)
        if sum(len(x) + 1 for x in current) > max_chars:
            chunks.append(" ".join(current))
            current = []
    if current:
        chunks.append(" ".join(current))
    return chunks