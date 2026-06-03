from flask import Flask, render_template, request
import os

app = Flask(__name__)

# =========================
# CSS QUESTIONS
# =========================

questions = [

{
    "question": "What does CSS stand for?",
    "options": [
        "Cascading Style Sheets",
        "Creative Style Sheets",
        "Computer Style Sheets",
        "Colorful Style Sheets"
    ],
    "answer": "Cascading Style Sheets"
},

{
    "question": "Which property changes text color?",
    "options": ["color", "font-color", "text-color", "background"],
    "answer": "color"
},

{
    "question": "Which property changes background color?",
    "options": [
        "background-color",
        "bgcolor",
        "color",
        "background-style"
    ],
    "answer": "background-color"
},

{
    "question": "Which property changes font size?",
    "options": ["font-size", "text-size", "size", "font-style"],
    "answer": "font-size"
},

{
    "question": "Which symbol selects class?",
    "options": [".", "#", "*", "$"],
    "answer": "."
},

{
    "question": "Which symbol selects id?",
    "options": ["#", ".", "*", "$"],
    "answer": "#"
},

{
    "question": "Which property aligns text center?",
    "options": ["text-align", "align", "center", "font-align"],
    "answer": "text-align"
},

{
    "question": "Which property changes font?",
    "options": ["font-family", "font-style", "font", "text-font"],
    "answer": "font-family"
},

{
    "question": "Which property adds inside spacing?",
    "options": ["padding", "margin", "space", "border"],
    "answer": "padding"
},

{
    "question": "Which property adds outside spacing?",
    "options": ["margin", "padding", "space", "border"],
    "answer": "margin"
},

{
    "question": "Which property makes text bold?",
    "options": ["font-weight", "bold", "font-style", "text-bold"],
    "answer": "font-weight"
},

{
    "question": "Which property adds shadow?",
    "options": ["box-shadow", "shadow", "text-shadow", "border-shadow"],
    "answer": "box-shadow"
},

{
    "question": "Which property rounds corners?",
    "options": ["border-radius", "corner-radius", "round", "radius"],
    "answer": "border-radius"
},

{
    "question": "Which property changes width?",
    "options": ["width", "size", "length", "w"],
    "answer": "width"
},

{
    "question": "Which property changes height?",
    "options": ["height", "size", "length", "h"],
    "answer": "height"
},

{
    "question": "Which display value creates flexbox?",
    "options": ["flex", "block", "inline", "grid"],
    "answer": "flex"
},

{
    "question": "Which property changes transparency?",
    "options": ["opacity", "transparent", "visibility", "display"],
    "answer": "opacity"
},

{
    "question": "Which property hides element?",
    "options": ["display:none", "hidden", "opacity", "remove"],
    "answer": "display:none"
},

{
    "question": "Which position keeps element fixed?",
    "options": ["fixed", "absolute", "relative", "sticky"],
    "answer": "fixed"
},

{
    "question": "Which property changes cursor style?",
    "options": ["cursor", "pointer", "mouse", "hover"],
    "answer": "cursor"
},

{
    "question": "Which property adds animation?",
    "options": ["animation", "transform", "transition", "motion"],
    "answer": "animation"
},

{
    "question": "Which property adds smooth effect?",
    "options": ["transition", "animation", "effect", "smooth"],
    "answer": "transition"
},

{
    "question": "Which property rotates element?",
    "options": ["transform", "rotate", "spin", "animation"],
    "answer": "transform"
},

{
    "question": "Which property changes layer order?",
    "options": ["z-index", "layer", "index", "order"],
    "answer": "z-index"
},

{
    "question": "Which selector selects all elements?",
    "options": ["*", ".", "#", "all"],
    "answer": "*"
},

{
    "question": "Which property controls overflow?",
    "options": ["overflow", "hidden", "clip", "outside"],
    "answer": "overflow"
},

{
    "question": "Which property changes list bullets?",
    "options": ["list-style", "bullet-style", "list-type", "style"],
    "answer": "list-style"
},

{
    "question": "Which property changes border color?",
    "options": ["border-color", "border", "outline", "color"],
    "answer": "border-color"
},

{
    "question": "Which property aligns flex items?",
    "options": [
        "justify-content",
        "align-items",
        "flex-align",
        "content-align"
    ],
    "answer": "justify-content"
},

{
    "question": "Which property changes text spacing?",
    "options": [
        "letter-spacing",
        "word-spacing",
        "spacing",
        "gap"
    ],
    "answer": "letter-spacing"
}

]

# =========================
# FILE
# =========================

FILE_NAME = "css_scores.txt"

if not os.path.exists(FILE_NAME):
    open(FILE_NAME, "w").close()

# =========================
# HOME PAGE
# =========================

@app.route("/")
def home():

    return render_template(
        "courses.html",
        questions=questions
    )

# =========================
# SUBMIT QUIZ
# =========================

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

            "options": q["options"],

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

        username=username,

        score=score,

        total=total,

        percentage=percentage,

        status=status,

        results=results

    )

# =========================
# LEADERBOARD
# =========================

@app.route("/leaderboard")
def leaderboard():

    data = []

    with open(FILE_NAME, "r") as file:

        for line in file:

            if "," in line:

                name, score = line.strip().split(",")

                data.append({

                    "username": name,

                    "score": int(score)

                })

    data = sorted(

        data,

        key=lambda x: x["score"],

        reverse=True

    )

    return render_template(

        "leaderboard.html",

        leaderboard=data

    )

# =========================
# RUN APP
# =========================

if __name__ == "__main__":

    app.run(debug=True)