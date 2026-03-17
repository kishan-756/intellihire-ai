skills_db = [
"python",
"java",
"c++",
"machine learning",
"data science",
"react",
"node",
"sql",
"mongodb",
"docker",
"kubernetes",
"aws",
"git",
"data structures",
"algorithms"
]


def extract_skills(text):

    text = text.lower()

    found = []

    for skill in skills_db:

        if skill in text:
            found.append(skill)

    return found


def analyze_skill_gap(resume_skills, job_skills):

    strong = []
    missing = []

    for skill in job_skills:

        skill = skill.strip()

        if skill in resume_skills:
            strong.append(skill)

        else:
            missing.append(skill)

    return strong, missing