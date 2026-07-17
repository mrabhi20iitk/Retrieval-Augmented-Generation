from langchain_community.vectorstores import FAISS

from src.text_splitter import chunks
from src.embeddings import embeddings

vectorstore = FAISS.from_documents(chunks,embeddings)
