from langchain.retrievers.multi_query import MultiQueryRetriever
from rag.retrieval.retrieval import retriever
from rag.generation.llm import llm


multi_query_retriever = MultiQueryRetriever.from_llm(retriever=retriever,
                                   llm=llm)