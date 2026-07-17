from src.rag_chain import rag_chain
import warnings 
warnings.filterwarnings('ignore')


query = input('Enter your query\n')

response = rag_chain.invoke(query)

print(response)