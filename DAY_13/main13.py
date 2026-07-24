# This is Day 13 project : Student Grade Manager

student_scores = input("Enter student scores separated by commas : ")
student_data = []

if not student_scores.strip():
    print("No scores entered.")
    exit()

try:
    scores = [int(score.strip()) for score in student_scores.split(",")]
except ValueError:
    print("Please enter only numbers.")
    exit()
    
for score in scores:
    if score < 0 or score > 100:
        print("Scores must be between 0 and 100.")
        exit()

sort_order = input("\nSort the scores in ascending or descending order (A/D) : ").upper()

grades = ["A" if score >= 90 else "B" if score >= 80 else "C" if score >= 70 else "D" if score >= 60 else "F" for score in scores]

def average_score(scores):
    return sum(scores) / len(scores)

print("\n------ Student Grades ------\n")

for index, score in enumerate(scores, start=1):
    student_data.append((index, score, grades[index - 1]))
    
if sort_order == "A":
    student_data.sort(key=lambda x: x[1])

elif sort_order == "D":
    student_data.sort(key=lambda x: x[1], reverse=True)
    
else:
    print("Invalid sort option.")
    exit()
    
for student_no, score, grade in student_data:
    print(f"Student {student_no} : Score = {score}, Grade = {grade}")
    
passing_students = [student for student in student_data if student[1] >= 60]
failing_students = [student for student in student_data if student[1] < 60]
    
print("\n------ Passing and Failing Students ------")

print("\nPassing Students :\n")
for student_no, score, grade in passing_students:
    print(f"Student {student_no}: {score} ({grade})")
    
print("\nFailing Students :\n")
for student_no, score, grade in failing_students:
    print(f"Student {student_no}: {score} ({grade})")

print("\n------ Average Score of Students ------\n")
print(f"Average : {average_score(scores):.2f}")

print("\n------ Highest and Lowest Mark ------\n")

highest_mark = max(student_data, key=lambda x: x[1])
lowest_mark = min(student_data, key=lambda x: x[1])

highest_student, highest_score, highest_grade = highest_mark
lowest_student, lowest_score, lowest_grade = lowest_mark

print(f"Highest Score")
print(f"Student {highest_student} : Score = {highest_score}, Grade = {highest_grade}")

print()

print(f"Lowest Score")
print(f"Student {lowest_student} : Score = {lowest_score}, Grade = {lowest_grade}")

# Done