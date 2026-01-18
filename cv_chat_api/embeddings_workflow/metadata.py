import os
from cv_chat_api.embeddings_workflow.pdf_reader import extract_text_from_pdf
from cv_chat_api.embeddings_workflow.chunk import simple_chunk
import numpy as np

class NaiveCandidateName:
    """A naive candidate name extractor that takes the first line of the text as the name."""

    def get(text: str) -> str:
        """Extracts the candidate's name from the first line of the text."""
        first_line = text.splitlines()[0].strip()
        return first_line

def process_pdf(index: int, filepath: str, candidate_name_extractor=NaiveCandidateName):
    chunk_text = []
    metadata = []
    ids = []
    text = extract_text_from_pdf(filepath)
    candidate_name = candidate_name_extractor.get(text)
    for chunk in simple_chunk(text):
        chunk_text.append(chunk)
        metadata.append(
            {
                "cv_id": filepath,
                "candidate_name": candidate_name,
                "id": index,
            }
        )
        ids.append(index)
        index += 1
    return chunk_text, metadata, ids, index

def process_pdf_files(directory: str):
    index = 0
    all_chunk_text = []
    all_metadata = []
    all_ids = []
    for filename in os.listdir(directory):
        if filename.endswith(".pdf"):
            filepath = os.path.join(directory, filename)
            chunk_text, metadata, ids, index = process_pdf(index, filepath)
            all_chunk_text.extend(chunk_text)
            all_metadata.extend(metadata)
            all_ids.extend(ids)
    return all_chunk_text, all_metadata, np.array(all_ids)


            
    
            
