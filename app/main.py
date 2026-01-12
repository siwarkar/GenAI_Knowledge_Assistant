from fastapi import FastAPI
from pydantic import BaseModel
from src.rag_chain import get_chain

app = FastAPI()
qa = get_chain()

class Q(BaseModel):
    question: str

@app.post("/ask")
def ask(q: Q):
    res = qa(q.question)
    return {"answer": res["result"]}
