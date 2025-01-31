import random
from typing import Dict, List

# Store the user's name (temporary storage for now)
user_name = ""

def save_user_name(name: str):
    """Stores the user's name in a global variable."""
    global user_name
    user_name = name

def get_all_questions() -> List[dict]:
    """Returns a list of all trivia questions."""
    return [
        {"id": 1, "question": "What is the best way to make a sandwich?", "options": ["Call your mom", "Buy one", "Make it yourself"], "correct_answer": 2},
        {"id": 2, "question": "Why do chickens cross the road?", "options": ["To get to the other side", "They are lost", "To join a gang"], "correct_answer": 0},
        {"id": 3, "question": "What is 2+2?", "options": ["Fish", "4", "A trick question"], "correct_answer": 1},
        {"id": 4, "question": "Who let the dogs out?", "options": ["Me", "You", "Nobody knows"], "correct_answer": 2},
        {"id": 5, "question": "How many ducks does it take to change a lightbulb?", "options": ["Ducks can't do that", "42", "Just one, a very skilled one"], "correct_answer": 0},
        {"id": 6, "question": "What happens when you microwave a spoon?", "options": ["A magic show", "An explosion", "Nothing"], "correct_answer": 1},
        {"id": 7, "question": "If you drop a cat, will it always land on its feet?", "options": ["Yes", "No", "Only if it's not watching"], "correct_answer": 2},
        {"id": 8, "question": "What is the secret ingredient in grandma's cookies?", "options": ["Love", "Cinnamon", "A legally questionable amount of butter"], "correct_answer": 2},
        {"id": 9, "question": "What is the best way to survive a zombie apocalypse?", "options": ["Run fast", "Stockpile snacks", "Make friends with the zombies"], "correct_answer": 2},
        {"id": 10, "question": "What is the most important rule of fight club?", "options": ["Don't talk about it", "Always bring snacks", "Wear a helmet"], "correct_answer": 0}
    ]

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