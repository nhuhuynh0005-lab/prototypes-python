import json
import os
from random import randint, sample, shuffle

# === DO NOT TOUCH ===

DIRNAME = os.path.dirname(os.path.abspath(__file__))
QUESTION_JSON_PATH = os.path.join(DIRNAME, "../questions.json")

with open(QUESTION_JSON_PATH, 'r') as file:
    raw_questions = json.load(file)

# === DO NOT TOUCH ===


def randomize_choices(choices: list[str], answer_idx: int) -> tuple[list[str], int]:
    """Shuffle the given list of choices and return a shuffled version and a new correct answer index."""
    if answer_idx < 0 or answer_idx >= len(choices):
        raise ValueError("invalid `answerIdx` given")
    new_choices = []
    new_answer_idx = randint(0, len(choices) - 1)

    for idx, choice in enumerate(choices):
        if idx != answer_idx:
            new_choices.append(choice)

    shuffle(new_choices)
    new_choices.insert(new_answer_idx, choices[answer_idx])

    return (new_choices, new_answer_idx)


class Question:
    prompt: str
    choices: list[str]
    _answer: int

    @staticmethod
    def from_dict(raw_data) -> "Question":
        q = Question()
        q.prompt = raw_data['prompt']
        q.choices, q._answer = randomize_choices(raw_data['choices'], 0)
        return q

    def is_correct(self, user_answer: str) -> bool:
        """Check whether the given answer is correct."""
        return user_answer.lower() == self._choice_label(self._answer).lower()

    def formatted_choices(self) -> str:
        """Return a formatted string containing the list of choices."""
        retval = ''
        for idx, choice in enumerate(self.choices):
            retval += f'{self._choice_label(idx)}. {choice}'
            if idx != len(self.choices) - 1:
                retval += '\n'

        return retval

    def correct_choice_label(self) -> str:
        return self._choice_label(self._answer)

    def _choice_label(self, idx: int) -> str:
        return chr(ord('A') + idx)


class Game:
    questions: list[Question]
    score: int
    _current_question_idx: int

    def __init__(self, questions: list[Question]):
        self.questions = questions
        self._current_question_idx = 0
        self.score = 0

    def run(self):
        current_question = self.questions[self._current_question_idx]
        print(current_question.prompt)
        print(current_question.formatted_choices())

        answer = ""
        while answer == "":
            answer = input("> ")

        if current_question.is_correct(answer):
            print('✅ Correct')
            self.score += 1
        else:
            print(
                f"❌ Incorrect. The correct answer is '{current_question.correct_choice_label()}'.")
        print('---')

        self._current_question_idx += 1

    def is_over(self):
        return self._current_question_idx >= len(self.questions)


NUM_QUESTIONS = 10

questions = []
for raw_question in sample(raw_questions, NUM_QUESTIONS):
    questions.append(Question.from_dict(raw_question))
game = Game(questions=questions)

while not game.is_over():
    game.run()

print(f"Final score: {game.score}.")
