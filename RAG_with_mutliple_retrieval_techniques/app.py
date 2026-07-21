from src.rag.chains.rag_chain import rag_chain

query = input('enter your query\n')

response = rag_chain.invoke(query)

print(response)