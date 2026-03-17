import random


aptitude_questions = [

{
"question":"What is 20% of 150?",
"options":["20","25","30","40"],
"answer":"30"
},

{
"question":"Probability of head in a fair coin?",
"options":["0","0.5","1","2"],
"answer":"0.5"
},

{
"question":"Average of 5,10,15?",
"options":["5","10","15","20"],
"answer":"10"
}

]


dsa_questions = [

{
"question":"Reverse a linked list",
"reference_answer":"Use three pointers prev, current, next to reverse links"
},

{
"question":"Detect cycle in linked list",
"reference_answer":"Use Floyd slow and fast pointer algorithm"
},

{
"question":"Find height of binary tree",
"reference_answer":"Use recursion max(left,right)+1"
}

]


hr_questions = [

{
"question":"Tell me about yourself",
"reference_answer":"Explain background, education and goals"
},

{
"question":"Why should we hire you?",
"reference_answer":"Explain skills and alignment with role"
},

{
"question":"What are your strengths?",
"reference_answer":"Mention technical strengths and examples"
}

]


def generate_interview(missing_skills):

    interview = {}

    interview["aptitude"] = random.choices(aptitude_questions, k=20)

    interview["dsa"] = random.sample(dsa_questions, 3)

    technical = []

    for skill in missing_skills[:5]:

        technical.append({

        "question": f"Explain {skill}",

        "reference_answer":
        f"{skill} is an important concept in software engineering. Explain its architecture, use cases and advantages."

        })

    interview["technical"] = technical

    interview["hr"] = random.sample(hr_questions, 3)

    return interview