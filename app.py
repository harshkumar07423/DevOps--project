from flask import Flask, render_template, request


QUESTIONS = [
    {
        "id": 1,
        "question": "What does CI stand for in DevOps?",
        "options": [
            "Continuous Integration",
            "Code Inspection",
            "Central Infrastructure",
            "Container Installation",
        ],
        "answer": 0,
    },
    {
        "id": 2,
        "question": "Which tool is commonly used to build container images?",
        "options": ["Docker", "Jenkins", "Git", "Terraform"],
        "answer": 0,
    },
    {
        "id": 3,
        "question": "What is the primary purpose of automated tests?",
        "options": [
            "Find regressions early",
            "Replace version control",
            "Deploy without code",
            "Increase server capacity",
        ],
        "answer": 0,
    },
    {
        "id": 4,
        "question": "Which command downloads a Git repository?",
        "options": ["git clone", "git merge", "git stash", "git diff"],
        "answer": 0,
    },
    {
        "id": 5,
        "question": "What does CD commonly mean in DevOps?",
        "options": [
            "Continuous Delivery",
            "Code Definition",
            "Change Documentation",
            "Central Deployment",
        ],
        "answer": 0,
    },
]

app = Flask(__name__, template_folder=".", static_folder=".", static_url_path="")


@app.get("/")
def home():
    return render_template("home.html")


@app.get("/quiz")
def quiz():
    return render_template("quiz.html", questions=QUESTIONS)


@app.post("/result")
def result():
    score = sum(
        request.form.get(f"question_{question['id']}", type=int) == question["answer"]
        for question in QUESTIONS
    )
    percentage = round(score / len(QUESTIONS) * 100)
    return render_template(
        "result.html",
        score=score,
        total=len(QUESTIONS),
        percentage=percentage,
    )


@app.get("/health")
def health():
    return {"status": "ok"}, 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)