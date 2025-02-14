from flask import Flask, render_template, request, session, redirect, url_for
from server_api import API
from random import sample
from logging import basicConfig, DEBUG, getLogger

logging_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
basicConfig(level=DEBUG)
logger = getLogger(__name__)

app = Flask(__name__)
app.secret_key = 'my_secret_key'

api = API()


@app.route("/questions")
def questions():
    return {"message": api.get_questions()}


@app.route("/questions/<int:num>")
def questions_num(num):
    return {"message": api.get_questions(num)}


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        num_questions = int(request.form.get('num_questions'))
        session['questions'] = sample(
            api.get_questions(num_questions), num_questions)
        session['current_question'] = 0
        session['score'] = 0
        return redirect(url_for('game'))
    return render_template('home.html')


@app.route('/game', methods=['GET', 'POST'])
def game():
    if 'questions' not in session or session['current_question'] >= len(
            session['questions']):
        return redirect(url_for('result'))

    if request.method == 'POST':
        selected_answer = request.form.get('answer')
        logger.info(f"selected answer: {selected_answer}")

        _questions: dict = session['questions']
        _current_question: dict = _questions[session['current_question']]
        _answer_index: int = _current_question['correct_answer']
        _correct_answer: str = _current_question['options'][_answer_index]

        logger.info(f"correct answer: {_correct_answer}")
        if selected_answer == _correct_answer:
            session['score'] += 1

        session['current_question'] += 1
        return redirect(url_for('game'))

    question_data = session['questions'][session['current_question']]
    return render_template(
        'game.html',
        question=question_data,
        question_number=session['current_question'] + 1,
        total=len(session['questions'])
        )


@app.route('/result')
def result():
    score = session.get('score', 0)
    total = len(session.get('questions', []))
    session.clear()
    return render_template('result.html', score=score, total=total)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
