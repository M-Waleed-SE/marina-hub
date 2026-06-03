from flask import Flask, render_template, request
import os

app = Flask(__name__)

# =========================
# 30 JAVASCRIPT QUESTIONS
# =========================

questions = [

{
    "question": "What is JavaScript used for?",
    "options": [
        "Styling",
        "Database",
        "Web Interactivity",
        "Server only"
    ],
    "answer": "Web Interactivity"
},

{
    "question": "Which keyword declares variable?",
    "options": ["var", "int", "string", "define"],
    "answer": "var"
},

{
    "question": "Which symbol is used for comments?",
    "options": ["//", "#", "<!-- -->", "**"],
    "answer": "//"
},

{
    "question": "Which function prints in console?",
    "options": [
        "console.log()",
        "print()",
        "display()",
        "show()"
    ],
    "answer": "console.log()"
},

{
    "question": "Which keyword creates function?",
    "options": ["function", "func", "define", "method"],
    "answer": "function"
},

{
    "question": "Which event occurs on button click?",
    "options": ["onclick", "onchange", "onmouse", "onsubmit"],
    "answer": "onclick"
},

{
    "question": "Which method selects element by id?",
    "options": [
        "getElementById()",
        "query()",
        "selectId()",
        "getId()"
    ],
    "answer": "getElementById()"
},

{
    "question": "Which keyword declares block variable?",
    "options": ["let", "var", "define", "int"],
    "answer": "let"
},

{
    "question": "Which keyword declares constant?",
    "options": ["const", "constant", "fixed", "final"],
    "answer": "const"
},

{
    "question": "Which operator compares value and type?",
    "options": ["===", "==", "=", "!="],
    "answer": "==="
},

{
    "question": "Which loop repeats code?",
    "options": ["for", "repeat", "loop", "foreach"],
    "answer": "for"
},

{
    "question": "Which statement handles conditions?",
    "options": ["if", "check", "condition", "switch"],
    "answer": "if"
},

{
    "question": "Which popup shows alert?",
    "options": ["alert()", "popup()", "message()", "warn()"],
    "answer": "alert()"
},

{
    "question": "Which method writes HTML content?",
    "options": [
        "innerHTML",
        "writeHTML",
        "htmlContent",
        "displayHTML"
    ],
    "answer": "innerHTML"
},

{
    "question": "Which keyword stops loop?",
    "options": ["break", "stop", "exit", "return"],
    "answer": "break"
},

{
    "question": "Which keyword skips iteration?",
    "options": ["continue", "skip", "next", "pass"],
    "answer": "continue"
},

{
    "question": "Which data type stores true/false?",
    "options": ["Boolean", "String", "Number", "Array"],
    "answer": "Boolean"
},

{
    "question": "Which method converts string to integer?",
    "options": ["parseInt()", "int()", "Number()", "convert()"],
    "answer": "parseInt()"
},

{
    "question": "Which method converts to lowercase?",
    "options": [
        "toLowerCase()",
        "lower()",
        "small()",
        "lowercase()"
    ],
    "answer": "toLowerCase()"
},

{
    "question": "Which method converts to uppercase?",
    "options": [
        "toUpperCase()",
        "upper()",
        "big()",
        "uppercase()"
    ],
    "answer": "toUpperCase()"
},

{
    "question": "Which method adds item to array end?",
    "options": ["push()", "add()", "append()", "insert()"],
    "answer": "push()"
},

{
    "question": "Which method removes last array item?",
    "options": ["pop()", "remove()", "delete()", "shift()"],
    "answer": "pop()"
},

{
    "question": "Which method joins array?",
    "options": ["join()", "merge()", "concat()", "connect()"],
    "answer": "join()"
},

{
    "question": "Which keyword creates object?",
    "options": ["new", "object", "create", "class"],
    "answer": "new"
},

{
    "question": "Which method delays code execution?",
    "options": [
        "setTimeout()",
        "delay()",
        "timeout()",
        "wait()"
    ],
    "answer": "setTimeout()"
},

{
    "question": "Which method repeats code continuously?",
    "options": [
        "setInterval()",
        "repeat()",
        "loop()",
        "timer()"
    ],
    "answer": "setInterval()"
},

{
    "question": "Which event occurs on page load?",
    "options": ["onload", "onclick", "onchange", "onopen"],
    "answer": "onload"
},

{
    "question": "Which operator means NOT equal?",
    "options": ["!=", "==", "=", "!==="],
    "answer": "!="
},

{
    "question": "Which keyword returns function value?",
    "options": ["return", "output", "result", "show"],
    "answer": "return"
},

{
    "question": "Which symbol concatenates strings?",
    "options": ["+", "&", "*", "."],
    "answer": "+"
}

]

FILE_NAME = "data.txt"

if not os.path.exists(FILE_NAME):
    open(FILE_NAME, "w").close()


@app.route("/")
def home():
    return render_template("courses.html", questions=questions)


@app.route("/submit", methods=["POST"])
def submit():

    username = request.form.get("username")

    score = 0
    results = []

    for i, q in enumerate(questions):

        user_answer = request.form.get(f"q{i}")
        correct_answer = q["answer"]

        if user_answer == correct_answer:
            score += 1

        results.append({
            "question": q["question"],
            "user_answer": user_answer,
            "correct_answer": correct_answer
        })

    total = len(questions)
    percentage = (score / total) * 100

    status = "PASS" if percentage >= 70 else "FAIL"

    with open(FILE_NAME, "a") as file:
        file.write(f"{username},{score}\n")

    return render_template(
        "result.html",
        score=score,
        total=total,
        results=results,
        percentage=percentage,
        status=status,
        username=username
    )


@app.route("/leaderboard")
def leaderboard():

    data = []

    with open(FILE_NAME, "r") as file:
        for line in file:
            name, score = line.strip().split(",")
            data.append({
                "username": name,
                "score": int(score)
            })

    data = sorted(data, key=lambda x: x["score"], reverse=True)

    return render_template("leaderboard.html", leaderboard=data)


if __name__ == "__main__":
    app.run(debug=True)