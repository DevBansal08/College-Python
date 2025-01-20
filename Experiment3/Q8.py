
name = input("Enter student's name: ")
roll_number = input("Enter roll number: ")
sapid = input("Enter SAPID: ")
sem = input("Enter semester: ")
course = input("Enter course: ")


pds = float(input("Enter marks for PDS: "))
python = float(input("Enter marks for Python: "))
chemistry = float(input("Enter marks for Chemistry: "))
english = float(input("Enter marks for English: "))
physics = float(input("Enter marks for Physics: "))


total_marks = pds + python + chemistry + english + physics
percentage = (total_marks / 500) * 100

cgpa = percentage / 10

if cgpa >= 9.1:
    grade = "O (Outstanding)"
elif cgpa >= 8.1:
    grade = "A+"
elif cgpa >= 7.1:
    grade = "A"
elif cgpa >= 6.1:
    grade = "B+"
elif cgpa >= 5.1:
    grade = "B"
elif cgpa >= 3.5:
    grade = "C+"
else:
    grade = "F"

print("\nGrade Sheet")
print(f"Name: {name}")
print(f"Roll Number: {roll_number}")
print(f"SAPID: {sapid}")
print(f"Sem: {sem}")
print(f"Course: {course}")
print(f"\nSubject marks:")
print(f"PDS: {pds}")
print(f"Python: {python}")
print(f"Chemistry: {chemistry}")
print(f"English: {english}")
print(f"Physics: {physics}")
print(f"\nPercentage: {percentage}%")
print(f"CGPA: {cgpa}")
print(f"Grade: {grade}")
