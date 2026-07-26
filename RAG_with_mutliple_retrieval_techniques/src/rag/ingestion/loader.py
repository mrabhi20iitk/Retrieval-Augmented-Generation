from langchain_community.document_loaders import PyPDFLoader

loader  = PyPDFLoader("../data/Thesis.pdf")

documents = loader.load()