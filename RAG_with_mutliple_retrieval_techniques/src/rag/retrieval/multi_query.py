from langchain.retrievers.multi_query import MultiQueryRetriever
from rag.retrieval.similarity import similarity_retriever
from rag.generation.llm import llm


multi_query_retriever = MultiQueryRetriever.from_llm(retriever=similarity_retriever,
                                   llm=llm)