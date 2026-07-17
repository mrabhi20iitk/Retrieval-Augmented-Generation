from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

from src.prompts import prompt
from src.llm import llm
from src.retriever import retriever





def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)


rag_chain = (
    {
        "context" : retriever | format_docs,
        "input" : RunnablePassthrough()
    }
    | prompt
    | llm
    | StrOutputParser()
)