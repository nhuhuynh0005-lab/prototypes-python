import json
import os
import random
import sys

# === DO NOT TOUCH ===

DIRNAME = os.path.dirname(os.path.abspath(__file__))
QUESTION_JSON_PATH = os.path.join(DIRNAME, "questions.json")

with open(QUESTION_JSON_PATH, 'r') as file:
    raw_questions = json.load(file)



# === DO NOT TOUCH ===
question_answer_list = random.sample(raw_questions, 10)
def format_question(question) -> str:
    choice_with_label = []
    for answer in question["choices"]:
        choice_with_label.append(answer)
    
    corect_answer = choice_with_label[0]
    random.shuffle(choice_with_label)

    a_list = []
    for ind, choice in enumerate(choice_with_label, start = 65 ):
        a_list.append(f"{chr(ind)}. {choice}")
        choices_str = "\n".join(a_list)
        answer_list = "".join(question['prompt']) + "\n" + choices_str
    return (
        answer_list,
        corect_answer,
        choice_with_label
        )
    
i = 0
for quiz in question_answer_list:
    ans_list,cor_answer,choice_with_label1 = format_question(quiz)
    print(ans_list)
     
    try:
        while True:
            input_keyword = input(">")
            if input_keyword.isalpha() and input_keyword in ["A","B","C","D"]  :
                input_keyword_int =ord(input_keyword)
                answer = choice_with_label1[input_keyword_int-65]
                if answer  ==  cor_answer :
                    print("✔ correct")
                    i += 1
                else :
                    print(f"✖ incorect.The correct answer is {chr(choice_with_label1.index(cor_answer) + 65)}")
                break
            else:
                if input_keyword == "":
                    continue
                else:
                    print(f"✖ incorect.The correct answer is {chr(choice_with_label1.index(cor_answer) + 65)}")
                    break
    except KeyboardInterrupt:
    
        sys.exit()
        
print(f"Your score is {i}/10")

