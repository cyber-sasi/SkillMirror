

from flask import Flask, render_template, request
from analyzer import analyze_github

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        username = request.form["username"]
        result = analyze_github(username)

        if result is None:
            return render_template("index.html", error="GitHub user not found")

        skills, summary = result

        # Temporary logic
        top_skill = skills[0]["language"] if skills else "N/A"
        consistency = "Medium"
        profile_type = "Skill Explorer"

        return render_template(
            "result.html",
            username=username,
            skills=skills,
            top_skill=top_skill,
            consistency=consistency,
            profile_type=profile_type
        )

    return render_template("index.html")


@app.route("/linkedin", methods=["GET", "POST"])
def linkedin():
    summary = ""
    skills = []

    if request.method == "POST":
        profile_text = request.form.get("profile_text", "")

        # Simple keyword-based skill detection
        skill_keywords = [
            "python", "java", "c++", "flask", "django",
            "html", "css", "javascript", "react",
            "machine learning", "data analysis", "sql"
        ]

        lower_text = profile_text.lower()

        for skill in skill_keywords:
            if skill in lower_text:
                skills.append(skill.title())

        if skills:
            summary = (
                f"Passionate professional with experience in {', '.join(skills)}. "
                "Strong focus on continuous learning, problem-solving, "
                "and real-world applications."
            )

    return render_template("linkedin.html", summary=summary, skills=skills)


if __name__ == "__main__":
    app.run()
