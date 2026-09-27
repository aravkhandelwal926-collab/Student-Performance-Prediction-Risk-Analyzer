from student import get_student_details
from marks import get_marks
from performance import calculate_percentage, performance_level, predict_performance
from risk_analyzer import check_risk
from recommendation import get_recommendations


print("Student Performance Prediction System and Risk Analyzer")

student = get_student_details()

subject = input("Enter subject: ")

marks = get_marks()

cat1 = marks[0]
cat2 = marks[1]
tee = marks[2]

attendance = float(input("Enter attendance percentage: "))

while attendance < 0 or attendance > 100:
    print("Invalid attendance. Enter a value between 0 and 100.")
    attendance = float(input("Enter attendance percentage: "))

total = cat1 + cat2 + tee

percentage = calculate_percentage(total)

performance = performance_level(percentage)

predicted = predict_performance(cat1, cat2, attendance)

risk = check_risk(percentage, attendance)

recommendations = get_recommendations(percentage, attendance)


print("\n----- RESULT -----")

print("Name:", student["name"])
print("Registration Number:", student["reg_no"])
print("Branch:", student["branch"])
print("Semester:", student["semester"])

print("Subject:", subject)

print("CAT 1:", cat1)
print("CAT 2:", cat2)
print("TEE:", tee)

print("Total:", total, "/ 200")
print("Percentage:", percentage, "%")
print("Performance:", performance)
print("Predicted Performance:", predicted, "%")
print("Attendance:", attendance, "%")
print("Risk:", risk)

print("\nRecommendations:")

for recommendation in recommendations:
    print("-", recommendation)

print("\nProgram completed.")