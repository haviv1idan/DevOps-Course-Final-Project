import random
from typing import Dict, List
from trivia_db import questions_list

# Store the user's name (temporary storage for now)
user_name = ""

def save_user_name(name: str):
    """Stores the user's name in a global variable."""
    global user_name
    user_name = name

def get_all_questions() -> List[dict]:
    """Returns a list of all trivia questions."""
    return questions_list

def get_random_questions(n: int) -> List[dict]:
    """Returns `n` random questions from the question list."""
    all_questions = get_all_questions()
    if n >= len(all_questions):
        return all_questions
    return random.sample(all_questions, n)

def check_answers(answers: List[Dict[str, int]]) -> int:
    """Checks user's answers and returns the number of correct responses.
    
    Expects a list of dictionaries:
    [
        {"question_id": 1, "answer_index": 0},
        {"question_id": 3, "answer_index": 2}
    ]
    """
    correct_count = 0
    all_questions = get_all_questions()

    # Create a dictionary for quick lookup of correct answers
    question_dict = {q["id"]: q["correct_answer"] for q in all_questions}

    for answer in answers:
        question_id = answer["question_id"]
        selected_index = answer["answer_index"]

        # Check if the question ID exists and if the answer is correct
        if question_id in question_dict and question_dict[question_id] == selected_index:
            correct_count += 1
    
    return correct_count