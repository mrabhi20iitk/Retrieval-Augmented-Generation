from langchain_community.document_loaders import PyPDFLoader


def loader(data):
    doc_loader = PyPDFLoader(data)
    docs = doc_loader.load()
    return docs