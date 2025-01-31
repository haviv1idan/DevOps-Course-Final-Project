from fastapi import FastAPI, HTTPException
from typing import Dict, List
from requests import save_user_name, get_all_questions, get_random_questions, check_answers

app = FastAPI()

@app.post("/user/")
def create_user(name: str):
    """Stores the user's name and returns a success message."""
    save_user_name(name)
    return {"message": f"Welcome, {name}!"}

@app.get("/questions/")
def get_questions():
    """Returns all trivia questions."""
    return get_all_questions()

@app.get("/questions/random/")
def get_random(n: int):
    """Returns `n` random questions from the question bank."""
    return get_random_questions(n)

@app.post("/answers/")
def submit_answers(answers: List[Dict[str, int]]):
    """Checks the user's answers and returns the number of correct responses.
    
    Expected JSON format:
    [
        {"question_id": 1, "answer_index": 0},
        {"question_id": 3, "answer_index": 2}
    ]
    """
    num_correct = check_answers(answers)
    return {"correct_answers": num_correct}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000, reload=True)
