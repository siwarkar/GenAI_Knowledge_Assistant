from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
from src.vector_store import load_store

def get_chain():
    retriever = load_store().as_retriever(search_kwargs={"k":3})
    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
    return RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
