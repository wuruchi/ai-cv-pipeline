from pathlib import Path
from cv_chat_api.embeddings_workflow.workflow import workflow

def test_workflow():
    directory = Path(__file__).parent
    all_chunk_text, all_metadata, embeddings, index, all_ids = workflow(directory)
    assert len(all_chunk_text) > 0
    assert len(all_metadata) > 0
    assert embeddings.shape[0] == len(all_chunk_text)
    assert len(all_ids) == len(all_chunk_text)