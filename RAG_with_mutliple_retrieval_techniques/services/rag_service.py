# services/rag_service.py

from rag.retrieval import retrievers
from rag.chains.rag_chain import build_rag_chain


def ask(question: str, retriever_name: str):

    retriever = retrievers.get(retriever_name)

    if retriever is None:
        raise ValueError("Invalid retriever")

    chain = build_rag_chain(retriever)

    return {
        "question": question,
        "retriever": retriever_name,
        "answer": chain.invoke(question)
    }