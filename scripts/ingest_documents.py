from src.loader import load_documents
from src.vector_store import create_store

docs = load_documents()
create_store(docs)
print("Documents ingested")

