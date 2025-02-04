import random
from json import load
from typing import Dict, List
from trivia_db import questions_list
from questions import Questions, Question
from functools import lru_cache

# Store the user's name (temporary storage for now)
user_name = ""

questions = Questions('questions.yaml')

def save_user_name(name: str):
    """Stores the user's name in a global variable."""
    global user_name
    user_name = name

@lru_cache(1)
def get_all_questions() -> Questions:
    """Returns a list of all trivia questions."""
    return questions


def get_random_question() -> Question:
    """Returns a random question from the question bank."""
    return questions.get_random_question()


def check_answer(answer: str, question: Question):
    """Checks the user's answer and returns True if it is correct."""
    return question.check_answer(answer)


