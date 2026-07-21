from langchain_community.document_loaders import PyPDFLoader

loader  = PyPDFLoader("../data/RBI_IT_manual.pdf")

documents = loader.load()