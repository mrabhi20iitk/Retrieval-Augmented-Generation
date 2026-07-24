from fastapi import FastAPI , HTTPException
from src.rag.chains.rag_chain import  rag_chain_similarity , rag_chain_hybrid , rag_chain_muti_query
from pydantic import BaseModel

class QueryRequest(BaseModel):
    retriever : str
    question: str


app = FastAPI()

retrievers = {
    "similarity" : rag_chain_similarity,
    "hybrid" : rag_chain_hybrid,
    "multi_query" : rag_chain_muti_query
}

@app.post("/query")
def response(query: QueryRequest):
    return {"question" : query.question,
            "answer" : retrievers[query.retriever].invoke(query.question) }

