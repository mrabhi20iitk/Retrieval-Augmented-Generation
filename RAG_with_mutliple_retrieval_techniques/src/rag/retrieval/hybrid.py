from langchain_community.retrievers import BM25Retriever
from langchain.retrievers import EnsembleRetriever
from rag.ingestion.loader import documents
from rag.vectorstore.store import vectorstore
from rag.retrieval.similarity import similarity_retriever



# Keyword retriever
bm25_retriever = BM25Retriever.from_documents(documents)
bm25_retriever.k = 5




# Hybrid retriever
hybrid_retriever = EnsembleRetriever(
    retrievers=[
        bm25_retriever,
        similarity_retriever
    ],
    weights=[
        0.4,
        0.6
    ]
)


