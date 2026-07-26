import json
import os

# === DO NOT TOUCH ===

DIRNAME = os.path.dirname(os.path.abspath(__file__))
QUESTION_JSON_PATH = os.path.join(DIRNAME, "questions.json")

with open(QUESTION_JSON_PATH, 'r') as file:
    raw_questions = json.load(file)

# === DO NOT TOUCH ===

print(raw_questions[0])
print(type(raw_questions[0]))
print(len(raw_questions))
