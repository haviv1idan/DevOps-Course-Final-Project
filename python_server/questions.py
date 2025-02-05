from random import choice
import random


class Questions:

    def __init__(self, questions_file: list[dict]):
        self.questions = questions_file or {}

    def get_all_questions(self) -> list[dict]:
        return self.questions
    
    def get_random_questions(self, n: int) -> list[dict]:
        """Returns `n` random questions from the question list."""
        if n >= len(self.questions):
            return self.questions
        return random.sample(self.questions, n)
