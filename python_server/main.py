from fastapi import FastAPI, HTTPException
from typing import Dict, List
from questions import Question
from api import save_user_name, get_all_questions

app = FastAPI()

@app.post("/user/")
def create_user(name: str):
    """Stores the user's name and returns a success message."""
    save_user_name(name)
    return {"message": f"Welcome, {name}!"}

@app.get("/questions/")
def get_questions():
    """Returns all trivia questions."""
    return [i.__str__ for i in get_all_questions()]

@app.get("/questions/random/")
def get_random(n: int) -> list[Question]:
    """Returns `n` random questions from the question bank."""
    return [get_all_questions().get_random_question() for i in range(n)]

@app.post("/check_answer/")
def submit_answers(answer: str, question: Question):
    """Checks the user's answers and returns the number of correct responses."""
    message = "Correct!" if question.check_answer(answer) else "Incorrct!"
    return {"message": message}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000, reload=True)
