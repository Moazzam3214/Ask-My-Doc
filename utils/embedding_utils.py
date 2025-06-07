import numpy as np
import faiss
import json
from sentence_transformers import SentenceTransformer


class Embedder:
    def __init__(self, model_name="all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)

    def embed_chunks(self, chunks):
        return self.model.encode(chunks)

    def save_index(self, embeddings, path="data/index.faiss"):
        embeddings = np.array(embeddings)
        dim = embeddings.shape[1]
        index = faiss.IndexFlatL2(dim)
        index.add(embeddings)
        faiss.write_index(index, path)

    def load_index(self, path="data/index.faiss"):
        return faiss.read_index(path)

    def save_chunks(self, chunks, path="data/chunks.json"):
        with open(path, "w") as f:
            json.dump(chunks, f)

    def load_chunks(self, path="data/chunks.json"):
        with open(path, "r") as f:
            return json.load(f)

    def search(self, index, query, chunks, top_k=5):
        query_emb = self.model.encode([query])
        distances, indices = index.search(query_emb, top_k)
        matched_chunks = [chunks[i] for i in indices[0]]
        return matched_chunks, distances

    def create_faiss_index(self, embeddings, dim):
        index = faiss.IndexFlatL2(dim)
        index.add(np.array(embeddings))
        return index
