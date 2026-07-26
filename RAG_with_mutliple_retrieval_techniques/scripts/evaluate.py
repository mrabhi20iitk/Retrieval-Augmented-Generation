from ragas.llms import LangchainLLMWrapper
from ragas.metrics import LLMContextRecall, Faithfulness, FactualCorrectness
from src.rag.generation.llm import llm 
from scripts.build_dataset import eval_dataset
from ragas import evaluate

evaluator_llm = LangchainLLMWrapper(llm)


result = evaluate(
    dataset=eval_dataset,
    metrics=[LLMContextRecall(), Faithfulness(), FactualCorrectness()],
    llm=evaluator_llm,
)

result