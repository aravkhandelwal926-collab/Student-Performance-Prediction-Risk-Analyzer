def check_risk(percentage, attendance):

    if percentage < 50 or attendance < 75:
        return "High Risk"

    elif percentage < 60 or attendance < 80:
        return "Medium Risk"

    else:
        return "Low Risk"