from fastapi import FastAPI
from questions import Questions
from trivia_db import questions_list


app = FastAPI()
questions = Questions(questions_list)


@app.get("/questions/")
def get_random(num: int = 0) -> list[dict]:
    """Returns `n` random questions from the question bank."""
    if num == 0:
        return questions.get_all_questions()
    return questions.get_random_questions(num)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000, reload=True)
