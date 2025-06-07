from utils.document_utils import read_file, clean_text, chunk_text
from utils.embedding_utils import Embedder
from utils.llm_utils import GoogleGemini


def run_pipeline(file_path, query):
    raw_text = read_file(file_path)
    cleaned = clean_text(raw_text)
    chunks = chunk_text(cleaned)

    embedder = Embedder()
    embeddings = embedder.embed_chunks(chunks)
    embedder.save_index(embeddings)
    embedder.save_chunks(chunks)

    index = embedder.load_index()
    stored_chunks = embedder.load_chunks()

    matched_chunks, _ = embedder.search(index, query, stored_chunks)
    context = "\n\n".join(matched_chunks)

    gemini = GoogleGemini()
    answer = gemini.ask(context, query)
    return answer


