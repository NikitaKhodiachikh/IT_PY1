import json


# TODO решите задачу
def task() -> float:
    file = "input.json"
    with open(file, 'r') as file:
        dict = json.load(file)
    summ = sum([item["score"] * item["weight"] for item in dict])
    return round(summ, 3)

print(task())
