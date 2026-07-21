from langchain_community.vectorstores import FAISS

from rag.ingestion.splitters import chunks
from rag.embeddings.embedding_model import embeddings

vectorstore = FAISS.from_documents(chunks,embeddings)

