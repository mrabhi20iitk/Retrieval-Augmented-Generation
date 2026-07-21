from fastapi import FastAPI , HTTPException
from src.rag.chains.rag_chain import rag_chain
from pydantic import BaseModel

class QueryRequest(BaseModel):
    question: str


app = FastAPI()

@app.post("/query")
def response(query: QueryRequest):
    response = rag_chain.invoke(query.question)
    return {"answer" : response}

