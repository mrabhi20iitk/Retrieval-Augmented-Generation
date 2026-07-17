
from langchain_groq import ChatGroq

from src.config import API_KEY




llm = ChatGroq(model='openai/gpt-oss-120b',api_key=API_KEY)

