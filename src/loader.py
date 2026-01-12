from langchain.document_loaders import PyPDFLoader, TextLoader
from pathlib import Path

def load_documents(path="data/documents"):
    docs = []
    for file in Path(path).iterdir():
        if file.suffix == ".pdf":
            docs.extend(PyPDFLoader(str(file)).load())
        elif file.suffix == ".txt":
            docs.extend(TextLoader(str(file)).load())
    return docs
