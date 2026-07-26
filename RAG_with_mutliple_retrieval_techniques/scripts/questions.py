import json

with open("../data/eval_data.json") as f:
    eval_data = json.load(f)


questions = []
ground_truth = []

for i in eval_data:
    questions.append(i["question"])
    ground_truth.append[i["answer"]]