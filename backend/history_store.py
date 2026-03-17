interview_history = []

def save_interview(email, aptitude, technical):

    interview_history.append({
        "email": email,
        "aptitude_score": aptitude,
        "technical_score": technical
    })


def get_history(email):

    user_history = []

    for item in interview_history:
        if item["email"] == email:
            user_history.append(item)

    return user_history