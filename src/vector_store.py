from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS

def create_store(docs):
    emb = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vs = FAISS.from_documents(docs, emb)
    vs.save_local("embeddings/faiss_index")

def load_store():
    emb = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    return FAISS.load_local("embeddings/faiss_index", emb)
