import streamlit as st
from utils.document_utils import read_file, clean_text, chunk_text
from utils.embedding_utils import Embedder
from utils.llm_utils import GoogleGemini
import tempfile
import os

st.set_page_config(page_title="📄 Document QA Chatbot", layout="centered")
st.title("🤖 AI Document QA Chatbot")

embedder = Embedder()
gemini = GoogleGemini()

if "state" not in st.session_state:
    st.session_state.state = None
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

with st.sidebar:
    uploaded_file = st.file_uploader(
        "📎 Upload PDF / DOCX / TXT", type=["pdf", "docx", "txt"])
    if uploaded_file is not None:
        ext = os.path.splitext(uploaded_file.name)[1]
        temp_path = tempfile.mktemp(suffix=ext)
        with open(temp_path, "wb") as f:
            f.write(uploaded_file.read())

        with st.spinner("📄 Processing document..."):
            raw_text = read_file(temp_path)
            cleaned = clean_text(raw_text)
            chunks = chunk_text(cleaned)

            embeddings = embedder.embed_chunks(chunks)
            dim = len(embeddings[0])
            index = embedder.create_faiss_index(embeddings, dim)

            st.session_state.state = {"chunks": chunks, "index": index}
            st.success("✅ Ready! Ask your question in the text box.")

for msg in st.session_state.chat_history:
    with st.chat_message(msg["role"]):
        st.markdown(msg["text"])

if st.session_state.state:
    user_input = st.chat_input("Ask something from the document...")
    if user_input:
        st.session_state.chat_history.append(
            {"role": "user", "text": user_input})
        with st.chat_message("user"):
            st.markdown(user_input)

        with st.chat_message("assistant"):
            with st.spinner("🤖 Thinking..."):
                matched_chunks, _ = embedder.search(
                    st.session_state.state["index"],
                    user_input,
                    st.session_state.state["chunks"]
                )
                context = "\n\n".join(matched_chunks)
                answer = gemini.ask(context, user_input)
                st.markdown(answer)

        st.session_state.chat_history.append(
            {"role": "assistant", "text": answer})
