from flask import Flask, render_template, request

app = Flask(__name__)

questions = [
    {
        "q": "What is 2 + 2?",
        "options": ["2", "4", "6", "8"],
        "answer": "4"
    },
    {
        "q": "Capital of India?",
        "options": ["Chennai", "Delhi", "Mumbai", "Kolkata"],
        "answer": "Delhi"
    }
]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/quiz", methods=["GET", "POST"])
def quiz():
    if request.method == "POST":
        score = 0
        for i in range(len(questions)):
            if request.form.get(str(i)) == questions[i]["answer"]:
                score += 1

        percentage = (score / len(questions)) * 100
        return render_template("result.html", score=score, total=len(questions), percentage=percentage)

    return render_template("quiz.html", questions=questions)

if __name__ == "__main__":
    app.run(debug=True)
