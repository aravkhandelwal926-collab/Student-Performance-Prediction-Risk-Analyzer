def get_recommendations(percentage, attendance):

    recommendations = []

    if percentage < 60:
        recommendations.append("Practice more and improve subject performance.")

    if attendance < 75:
        recommendations.append("Try to improve attendance.")

    if len(recommendations) == 0:
        recommendations.append("Keep up the good work.")

    return recommendations