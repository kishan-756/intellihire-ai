sessions = {}

def start_session(interview):

    session_id = len(sessions) + 1

    sessions[session_id] = {
        "interview": interview,
        "answers": [],
        "score": 0
    }

    return session_id


def save_answer(session_id, question, score):

    session = sessions.get(session_id)

    if not session:
        return

    session["answers"].append({
        "question": question,
        "score": score
    })

    session["score"] += score


def get_report(session_id):

    session = sessions.get(session_id)

    if not session:
        return None

    total = len(session["answers"])

    avg = session["score"] / total if total else 0

    return {
        "total_questions": total,
        "average_score": avg,
        "answers": session["answers"]
    }