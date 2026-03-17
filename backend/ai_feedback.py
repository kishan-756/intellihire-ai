def analyze_performance(aptitude, dsa, technical):

    weaknesses = []
    recommendations = []

    if aptitude < 10:
        weaknesses.append("Aptitude")
        recommendations.append("Practice quantitative aptitude and logical reasoning")

    if dsa < 2:
        weaknesses.append("Data Structures")
        recommendations.append("Practice linked lists, stacks, queues")

    if technical < 3:
        weaknesses.append("Technical Concepts")
        recommendations.append("Revise core CS topics and system design basics")

    return {
        "weaknesses": weaknesses,
        "recommendations": recommendations
    }