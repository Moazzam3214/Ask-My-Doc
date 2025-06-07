# Ask My Doc 🤖

An AI-powered web application that lets you upload documents (PDF, DOCX, TXT) and ask questions about their content. The app uses semantic search with sentence embeddings and Google Gemini LLM to provide concise, context-aware answers in a modern chat interface.

---

## 🎯 Features

* **Document QA:** Upload a document and ask questions about its content.
* **Semantic Search:** Finds the most relevant text chunks using sentence embeddings and FAISS.
* **LLM-Powered Answers:** Uses Google Gemini to generate concise, relevant answers from context.
* **Multi-format Support:** Accepts PDF, DOCX, and TXT files.
* **Modern Web UI:** Built with Streamlit for an interactive chat experience.
* **Session Memory:** Maintains chat history for each session.

---

## 📁 Project Structure

```
ask-my-doc/
├── app.py                     # Streamlit web application
├── main.py                    # Pipeline for document QA
├── utils/
│   ├── document_utils.py      # File reading, cleaning, chunking
│   ├── embedding_utils.py     # Embedding and FAISS index utilities
│   └── llm_utils.py           # Google Gemini integration
├── requirements.txt
├── .env                       # API keys and environment variables
├── .gitignore
├── experiments.ipynb          # Prototyping and experiments
```

---

## 🛠️ Installation

Clone the repository:

```sh
git clone https://github.com/moazzam3214/ask-my-doc.git
cd ask-my-doc
```

Create a virtual environment (recommended):

```sh
python -m venv venv
# On Unix/macOS:
source venv/bin/activate
# On Windows:
venv\Scripts\activate
```

Install dependencies:

```sh
pip install -r requirements.txt
```

Set up your `.env` file with your Google Gemini API key:

```
GOOGLE_API_KEY=your-gemini-api-key
```

---

## 🚀 Quick Start

Run the Streamlit app:

```sh
streamlit run app.py
```

Open your browser and navigate to [http://localhost:8501](http://localhost:8501)

* Upload a PDF, DOCX, or TXT document.
* Wait for processing, then ask questions in the chat box.
* Get concise, context-aware answers from the AI.

---

## 🧠 How It Works

* **Document Parsing:** Reads and cleans text from PDF, DOCX, or TXT files.
* **Chunking:** Splits text into overlapping chunks for semantic search.
* **Embedding:** Uses Sentence Transformers to embed chunks.
* **Semantic Search:** Finds the most relevant chunks using FAISS.
* **LLM Answering:** Sends context and question to Gemini for answer generation.

---

## 🎮 Usage Example (Python)

You can use the pipeline directly in Python:

```python
from main import run_pipeline

answer = run_pipeline("your_document.pdf", "What is this document about?")
print(answer)
```

---

## 📋 Requirements

* Python 3.9+
* Streamlit
* pandas, numpy
* PyMuPDF
* python-docx
* sentence-transformers
* faiss-cpu
* google-generativeai
* python-dotenv

See `requirements.txt` for details.

---

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Make your changes
4. Commit: `git commit -m 'Add amazing feature'`
5. Push: `git push origin feature/amazing-feature`
6. Open a Pull Request

**Areas for Improvement:**

* Add support for more file types
* Improve chunking and context selection
* Add user authentication
* Enhance UI/UX

---

## 📈 Future Enhancements

* Multi-document support
* Real-time document updates
* Advanced analytics dashboard
* Integration with cloud storage

---

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 🙏 Acknowledgments

* [Streamlit](https://streamlit.io/)
* [Sentence Transformers](https://www.sbert.net/)
* [Google Gemini](https://ai.google.dev/)
* [FAISS](https://faiss.ai/)
* Open source community

---

## 📞 Contact

GitHub: [@Moazzam3214](https://github.com/Moazzam3214)  
Email: [moazzamaleem786@gmail.com](mailto:moazzamaleem786@gmail.com)  
LinkedIn: [Muhammad Moazzam](https://www.linkedin.com/in/muhammad-moazzam-492b0724b/)

⭐ Star this repository if you found it helpful!

Made with ❤️ and lots of ☕