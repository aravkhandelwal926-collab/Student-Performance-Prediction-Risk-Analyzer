def get_student_details():
    student = {}

    student["name"] = input("Enter name: ")
    student["reg_no"] = input("Enter registration number: ")
    student["branch"] = input("Enter branch: ")
    student["semester"] = input("Enter semester: ")

    return student