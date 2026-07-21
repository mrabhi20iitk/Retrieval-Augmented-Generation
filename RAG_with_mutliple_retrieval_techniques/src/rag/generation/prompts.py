from langchain.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_template(
    """
    You are a helpful assistant.

    Answer the question using the provided context.

    If the answer can be reasonably inferred from the context,
    provide the answer.

    If the context truly does not contain enough information,
    say "I don't know".

    Context:
    {context}

    Question:
    {input}
    """
)
