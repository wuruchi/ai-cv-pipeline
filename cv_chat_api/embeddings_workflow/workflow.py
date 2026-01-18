from cv_chat_api.embeddings_workflow.metadata import process_pdf_files
from cv_chat_api.embeddings_workflow.embeddings import get_embedding

def workflow(directory: str):
    """
    Complete workflow to process PDF files in a directory,
    extract text, generate embeddings, and return metadata.

    Args:
        directory (str): Path to the directory containing PDF files.
    Returns:
        tuple: (all_chunk_text, all_metadata, embeddings, index, all_ids)
    """
    all_chunk_text, all_metadata, all_ids = process_pdf_files(directory)
    embeddings, index = get_embedding(all_chunk_text)
    return all_chunk_text, all_metadata, embeddings, index, all_ids