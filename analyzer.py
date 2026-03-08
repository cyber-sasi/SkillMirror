import requests
import os

def analyze_github(username):
    username = username.strip()

    url = f"https://api.github.com/users/{username}/repos"

    # Get GitHub token if available (useful for Render deployment)
    token = os.getenv("GITHUB_TOKEN")

    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "SkillMirror-App"
    }

    if token:
        headers["Authorization"] = f"Bearer {token}"

    try:
        response = requests.get(url, headers=headers)
        print("GitHub API Status:", response.status_code)

        if response.status_code == 404:
            print("GitHub user not found")
            return None

        if response.status_code != 200:
            print("GitHub API error occurred:", response.text)
            return None

        repos = response.json()

    except Exception as e:
        print("Request failed:", str(e))
        return None

    languages = {}
    total_repos = len(repos)

    for repo in repos:
        lang = repo.get("language")
        if lang:
            languages[lang] = languages.get(lang, 0) + 1

    def get_skill_level(count):
        if count <= 2:
            return "Beginner"
        elif count <= 5:
            return "Intermediate"
        else:
            return "Advanced"

    def get_consistency(total):
        if total <= 3:
            return "Low"
        elif total <= 7:
            return "Medium"
        else:
            return "High"

    def get_profile_type(lang_dict):
        if not lang_dict:
            return "No Data"

        max_count = max(lang_dict.values())

        if max_count >= 5:
            return "Specialist"
        elif len(lang_dict) >= 3:
            return "Explorer"
        else:
            return "Balanced"

    skills = []

    for lang, count in languages.items():
        skills.append({
            "language": lang,
            "count": count,
            "level": get_skill_level(count)
        })

    summary = {
        "top_skill": max(languages, key=languages.get) if languages else "N/A",
        "consistency": get_consistency(total_repos),
        "profile": get_profile_type(languages),
        "total_repos": total_repos
    }

    return skills, summary
