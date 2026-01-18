from typing import List, Dict

def build_prompt(question:str, contexts: List[Dict]) -> str:
    context_blocks = []
    for c in contexts:
        block = (
            f"CV_ID: {c['cv_id']}\n"
            f"Candidate Name: {c['candidate_name']}\n"
            f"Excerpt: {c['chunk_text']}\n"
        )
        context_blocks.append(block)
    context_str = "\n---\n".join(context_blocks)

    return f"""
    You are an assistant that answers questions about job candidates based ONLY on the provided CV excerpts.

    Context:
    {context_str}

    Instructions:
    - Use only the facts in the context.
    - If the answer is not in the context, say you don't know.
    - When listing candidates, always mention their name and CV_ID.

    User question:
    {question}
    """