from openai import OpenAI

client = OpenAI()

def extract_job_skills(job_description):

    prompt = f"""
Extract only the technical skills from the following job description.

Return the result as a simple comma separated list.

Job Description:
{job_description}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role":"user","content":prompt}]
    )

    skills = response.choices[0].message.content

    return skills.lower().split(",")