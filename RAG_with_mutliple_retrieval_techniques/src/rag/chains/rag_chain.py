from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from rag.retrieval.retrieval import retriever
from rag.generation.llm import llm
from rag.generation.prompts import prompt


def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

rag_chain = (
    {"context" : retriever | format_docs,
     "input" : RunnablePassthrough() 
    }
    | prompt
    | llm
    | StrOutputParser()
)