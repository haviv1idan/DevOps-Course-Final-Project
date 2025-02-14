from flask import Flask, render_template
from server_api import API

app = Flask(__name__)

api = API()


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/questions")
def questions():
    return {"message": api.get_questions()}


@app.route("/questions/<int:num>")
def questions_num(num):
    return {"message": api.get_questions(num)}


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
