from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from rag.retrieval.similarity import similarity_retriever
from rag.retrieval.multi_query import multi_query_retriever
from rag.retrieval.hybrid import hybrid_retriever
from rag.generation.llm import llm
from rag.generation.prompts import prompt


def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)


def build_rag_chain(retriever):
    chain = (
        {"context": retriever | format_docs,
         "input" : RunnablePassthrough() }
         | prompt
         |llm
         | StrOutputParser()
        )
    return chain


