from langchain_community.retrievers import BM25Retriever
from langchain.retrievers import EnsembleRetriever
from rag.ingestion.loader import documents
from rag.vectorstore.store import vectorstore

# Keyword retriever
bm25_retriever = BM25Retriever.from_documents(documents)
bm25_retriever.k = 5


# Semantic retriever
faiss_retriever = vectorstore.as_retriever(
    search_kwargs={
        "k": 5
    }
)


# Hybrid retriever
hybrid_retriever = EnsembleRetriever(
    retrievers=[
        bm25_retriever,
        faiss_retriever
    ],
    weights=[
        0.4,
        0.6
    ]
)