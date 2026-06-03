from flask import Flask, render_template, request
import os

app = Flask(__name__)

# =========================
# 30 HTML QUESTIONS
# =========================

questions = [

{
    "question": "What does HTML stand for?",
    "options": [
        "Hyper Text Markup Language",
        "High Text Machine Language",
        "Hyperlinks Text Mark Language",
        "Home Tool Markup Language"
    ],
    "answer": "Hyper Text Markup Language"
},

{
    "question": "Which tag creates a paragraph?",
    "options": ["<p>", "<para>", "<text>", "<paragraph>"],
    "answer": "<p>"
},

{
    "question": "Which tag is used for images?",
    "options": ["<img>", "<image>", "<picture>", "<src>"],
    "answer": "<img>"
},

{
    "question": "Which tag creates a hyperlink?",
    "options": ["<a>", "<link>", "<href>", "<url>"],
    "answer": "<a>"
},

{
    "question": "Which tag creates a line break?",
    "options": ["<br>", "<break>", "<lb>", "<newline>"],
    "answer": "<br>"
},

{
    "question": "Which tag is used for headings?",
    "options": ["<h1>", "<heading>", "<head>", "<title>"],
    "answer": "<h1>"
},

{
    "question": "Which attribute gives image path?",
    "options": ["src", "href", "link", "path"],
    "answer": "src"
},

{
    "question": "Which tag creates unordered list?",
    "options": ["<ul>", "<ol>", "<li>", "<list>"],
    "answer": "<ul>"
},

{
    "question": "Which tag creates ordered list?",
    "options": ["<ol>", "<ul>", "<li>", "<list>"],
    "answer": "<ol>"
},

{
    "question": "Which tag creates table row?",
    "options": ["<tr>", "<td>", "<th>", "<table>"],
    "answer": "<tr>"
},

{
    "question": "Which tag creates table data?",
    "options": ["<td>", "<tr>", "<th>", "<table>"],
    "answer": "<td>"
},

{
    "question": "Which tag creates table heading?",
    "options": ["<th>", "<td>", "<tr>", "<table>"],
    "answer": "<th>"
},

{
    "question": "Which tag creates forms?",
    "options": ["<form>", "<input>", "<button>", "<label>"],
    "answer": "<form>"
},

{
    "question": "Which input type hides password?",
    "options": ["password", "text", "hidden", "secure"],
    "answer": "password"
},

{
    "question": "Which tag is used for comments?",
    "options": ["<!-- -->", "//", "#", "/* */"],
    "answer": "<!-- -->"
},

{
    "question": "Which tag creates buttons?",
    "options": ["<button>", "<btn>", "<click>", "<input>"],
    "answer": "<button>"
},

{
    "question": "Which tag creates dropdown list?",
    "options": ["<select>", "<dropdown>", "<choice>", "<option>"],
    "answer": "<select>"
},

{
    "question": "Which tag defines dropdown option?",
    "options": ["<option>", "<item>", "<select>", "<choice>"],
    "answer": "<option>"
},

{
    "question": "Which tag plays video?",
    "options": ["<video>", "<media>", "<movie>", "<play>"],
    "answer": "<video>"
},

{
    "question": "Which tag plays audio?",
    "options": ["<audio>", "<sound>", "<music>", "<mp3>"],
    "answer": "<audio>"
},

{
    "question": "Which HTML version is latest?",
    "options": ["HTML5", "HTML4", "HTML3", "XHTML"],
    "answer": "HTML5"
},

{
    "question": "Which tag contains webpage body?",
    "options": ["<body>", "<head>", "<main>", "<section>"],
    "answer": "<body>"
},

{
    "question": "Which tag contains metadata?",
    "options": ["<head>", "<meta>", "<body>", "<title>"],
    "answer": "<head>"
},

{
    "question": "Which tag defines webpage title?",
    "options": ["<title>", "<head>", "<meta>", "<body>"],
    "answer": "<title>"
},

{
    "question": "Which tag creates navigation?",
    "options": ["<nav>", "<navbar>", "<menu>", "<links>"],
    "answer": "<nav>"
},

{
    "question": "Which tag defines footer?",
    "options": ["<footer>", "<bottom>", "<end>", "<section>"],
    "answer": "<footer>"
},

{
    "question": "Which tag defines header?",
    "options": ["<header>", "<top>", "<head>", "<section>"],
    "answer": "<header>"
},

{
    "question": "Which tag groups elements?",
    "options": ["<div>", "<group>", "<section>", "<span>"],
    "answer": "<div>"
},

{
    "question": "Which attribute opens link in new tab?",
    "options": [
        "target='_blank'",
        "new='tab'",
        "tab='new'",
        "open='new'"
    ],
    "answer": "target='_blank'"
},

{
    "question": "Which tag is inline?",
    "options": ["<span>", "<div>", "<section>", "<article>"],
    "answer": "<span>"
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