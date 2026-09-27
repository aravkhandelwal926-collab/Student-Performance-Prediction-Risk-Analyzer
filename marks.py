def get_marks():
    marks = []

    cat1 = int(input("Enter CAT 1 marks (out of 50): "))
    while cat1 < 0 or cat1 > 50:
        print("Invalid marks. CAT 1 must be between 0 and 50.")
        cat1 = int(input("Enter CAT 1 marks (out of 50): "))

    marks.append(cat1)

    cat2 = int(input("Enter CAT 2 marks (out of 50): "))
    while cat2 < 0 or cat2 > 50:
        print("Invalid marks. CAT 2 must be between 0 and 50.")
        cat2 = int(input("Enter CAT 2 marks (out of 50): "))

    marks.append(cat2)

    tee = int(input("Enter TEE marks (out of 100): "))
    while tee < 0 or tee > 100:
        print("Invalid marks. TEE must be between 0 and 100.")
        tee = int(input("Enter TEE marks (out of 100): "))

    marks.append(tee)

    return marks