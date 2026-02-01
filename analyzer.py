# import requests

# username = input("Enter GitHub username: ")

# url = f"https://api.github.com/users/{username}/repos"
# response = requests.get(url)

# if response.status_code != 200:
#     print("GitHub user not found")
#     exit()

# repos = response.json()

# languages = {}
# total_repos = len(repos)

# for repo in repos:
#     lang = repo["language"]
#     if lang:
#         languages[lang] = languages.get(lang, 0) + 1


# def get_skill_level(count):
#     if count <= 2:
#         return "Beginner"
#     elif count <= 5:
#         return "Intermediate"
#     else:
#         return "Advanced"


# def get_consistency(total):
#     if total <= 3:
#         return "Low"
#     elif total <= 7:
#         return "Medium"
#     else:
#         return "High"


# def get_profile_type(lang_dict):
#     if not lang_dict:
#         return "No Data"

#     max_count = max(lang_dict.values())
#     dominant_langs = [l for l, c in lang_dict.items() if c == max_count]

#     if max_count >= 5:
#         return "Specialist"
#     elif len(lang_dict) >= 3:
#         return "Explorer"
#     else:
#         return "Balanced"


# # -------- OUTPUT --------
# print("\nSkillMirror Report")
# print("-------------------")
# print("GitHub User:", username)
# print("Total Repositories:", total_repos)

# print("\nDetected Skills:")
# for lang, count in languages.items():
#     level = get_skill_level(count)
#     print(f"{lang} → {count} projects → Skill Level: {level}")

# # Overall Summary
# top_skill = max(languages, key=languages.get) if languages else "N/A"
# consistency = get_consistency(total_repos)
# profile = get_profile_type(languages)

# print("\nOverall Skill Summary")
# print("----------------------")
# print("Top Skill:", top_skill)
# print("Consistency Level:", consistency)
# print("Learning Profile:", profile)
import requests

def analyze_github(username):
    url = f"https://api.github.com/users/{username}/repos"
    response = requests.get(url)

    if response.status_code != 200:
        return None

    repos = response.json()
    languages = {}
    total_repos = len(repos)

    for repo in repos:
        lang = repo["language"]
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
