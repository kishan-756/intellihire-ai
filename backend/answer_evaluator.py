from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer("all-MiniLM-L6-v2")


def evaluate_answer(user_answer, reference_answer):

    emb1 = model.encode([user_answer])
    emb2 = model.encode([reference_answer])

    score = cosine_similarity(emb1, emb2)[0][0]

    return float(score)