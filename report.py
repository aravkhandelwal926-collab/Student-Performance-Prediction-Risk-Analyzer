def show_report(name, subject, cat1, cat2, tee, total, percentage,
                attendance, risk, problems, recommendations):

    print("\n==============================")
    print(" STUDENT PERFORMANCE REPORT")
    print("==============================")

    print("Student Name:", name)
    print("Subject:", subject)

    print("\nMarks")
    print("CAT 1:", cat1, "/ 50")
    print("CAT 2:", cat2, "/ 50")
    print("TEE:", tee, "/ 100")
    print("Total:", total, "/ 200")
    print("Percentage:", percentage, "%")
    print("Attendance:", attendance, "%")

    print("\nRisk Level:", risk)

    if len(problems) > 0:
        print("\nProblems:")
        for problem in problems:
            print("-", problem)
    else:
        print("\nProblems: None")

    if len(recommendations) > 0:
        print("\nRecommendations:")
        for recommendation in recommendations:
            print("-", recommendation)
    else:
        print("\nRecommendations: None")

    print("==============================")