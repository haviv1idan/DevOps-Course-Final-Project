from uuid import uuid4
from random import choice
from yaml import safe_load

class Question:

    def __init__(self, question: str, options: list[str], answer: int):
        self.question = question
        self.options = options
        self.answer = self.options[answer]

    def __str__(self):
        return f"Question: {self.question}, Options: {self.options}, Answer: {self.answer}"
    
    def check_answer(self, answer: str) -> bool:
        return self.answer == answer


class Questions:

    def __init__(self, questions_file: str):
        if questions_file:
            self.get_questions_from_file(questions_file)
        else:
            self.questions = {}
    
    def get_questions_from_file(self, questions_file: str):
        with open(questions_file, 'r') as file:
            questions: list[dict] = safe_load(file)

        self.questions = {uuid4().hex: Question(q["question"], q["options"], q["answer"]) for q in questions}
    
    def add_question(self, question: Question):
        question_id = uuid4().hex
        self.questions[question_id] = question

    def get_all_questions(self) -> dict:
        return self.questions
    
    def get_random_question(self) -> Question:
        return self.questions[choice(list(self.questions.keys()))]
    