from .similarity import similarity_retriever
from .hybrid import hybrid_retriever , bm25_retriever
from .mmr import mmr_retriever
from .multi_query import multi_query_retriever

retrievers = {
    "similarity": similarity_retriever,
    "hybrid": hybrid_retriever,
    "bm25": bm25_retriever,
    "mmr" : mmr_retriever,
    "multi_query": multi_query_retriever
}