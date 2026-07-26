from ragas import EvaluationDataset
from scripts.questions import questions , ground_truth

from src.rag.retrieval import retrievers




from services.rag_service import ask

dataset = []


for queries, reference in zip(questions, ground_truth):
    relevant_docs = retrievers["similarity"].invoke(queries)

    answer = ask(queries,"similarity")["answer"]

    dataset.append({
        "user_input" : queries,
        "retrieved_contexts" : [doc.page_content for doc in relevant_docs ],
        "response" :  answer ,
        "reference" : reference
    })



eval_dataset = EvaluationDataset.from_list(dataset)