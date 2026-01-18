from pathlib import Path
from cv_chat_api.embeddings_workflow.pdf_reader import extract_text_from_pdf
from cv_chat_api.embeddings_workflow.metadata import NaiveCandidateName

def test_extract_text_from_pdf():
    pdf_path = Path(__file__).parent / "sample.pdf"
    text = extract_text_from_pdf(pdf_path)
    assert "Senior Backend Developer" in text
    assert "Strong advocate for clean code and best practices" in text

def test_candidate_name_extractor():
    pdf_path = Path(__file__).parent / "sample.pdf"
    text = extract_text_from_pdf(pdf_path)
    candidate_name = NaiveCandidateName.get(text)
    assert candidate_name == "Alba Martínez"