from pathlib import Path
from cv_chat_api.embeddings_workflow.pdf_reader import extract_text_from_pdf
from cv_chat_api.embeddings_workflow.chunk import simple_chunk

def test_chunk_process():
    pdf_path = Path(__file__).parent / "sample.pdf"
    text = extract_text_from_pdf(pdf_path)
    chunks = simple_chunk(text, 50)
    assert len(chunks) > 0