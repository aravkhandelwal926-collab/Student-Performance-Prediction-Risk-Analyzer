def calculate_percentage(total):
    return total / 2


def performance_level(percentage):
    if percentage >= 80:
        return "Excellent"
    elif percentage >= 70:
        return "Very Good"
    elif percentage >= 60:
        return "Good"
    elif percentage >= 50:
        return "Average"
    else:
        return "Needs Improvement"


def predict_performance(cat1, cat2, attendance):
    predicted_score = ((cat1 + cat2) * 0.8) + (attendance * 0.2)
    return round(predicted_score, 2)