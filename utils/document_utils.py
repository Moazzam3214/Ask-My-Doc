import fitz
import os
from docx import Document  


def read_pdf(pdf_path):
    text = ""
    with fitz.open(pdf_path) as doc:
        for page in doc:
            text += page.get_text()
    return text


def read_docx(docx_path):
    doc = Document(docx_path)
    full_text = [para.text for para in doc.paragraphs]
    return '\n'.join(full_text)


def read_txt(txt_path):
    with open(txt_path, 'r', encoding='utf-8') as f:
        return f.read()


def read_file(file_path):
    ext = os.path.splitext(file_path)[1].lower()
    if ext == '.pdf':
        return read_pdf(file_path)
    elif ext == '.docx':
        return read_docx(file_path)
    elif ext == '.txt':
        return read_txt(file_path)
    else:
        raise ValueError(f"Unsupported file format: {ext}")


def clean_text(text):
    text = text.lower()
    text = text.replace('\n', ' ')
    text = ''.join(c for c in text if c.isprintable()
                   and not (0xE000 <= ord(c) <= 0xF8FF))
    return text.strip()


def chunk_text(text, chunk_size=300, overlap=50):
    words = text.split()
    chunks = []
    start = 0
    while start < len(words):
        end = start + chunk_size
        chunk = words[start:end]
        chunks.append(' '.join(chunk))
        start += chunk_size - overlap
    return chunks
