
from rag.vectorstore.store import vectorstore

similarity_retriever = vectorstore.as_retriever(
    search_kwargs={"k":8}  # returning top 8 chunks
)