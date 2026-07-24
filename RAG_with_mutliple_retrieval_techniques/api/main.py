from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from services.rag_service import ask


class QueryRequest(BaseModel):
    retriever: str
    question: str


app = FastAPI()


@app.post("/query")
def query(request: QueryRequest):

    try:
        return ask(
            question=request.question,
            retriever_name=request.retriever
        )

    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )