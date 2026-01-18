from pathlib import Path
from cv_chat_api.embeddings_workflow.pdf_reader import extract_text_from_pdf
from cv_chat_api.embeddings_workflow.chunk import SimpleChunker

def test_chunk_process():
    pdf_path = Path(__file__).parent / "sample.pdf"
    text = extract_text_from_pdf(pdf_path)
    chunker = SimpleChunker(50)
    chunks = chunker.chunk(text)
    assert len(chunks) > 0