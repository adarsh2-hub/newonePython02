
# Student Marks Analyzer Project

students = [
    {"name": "Adarsh", "marks": [95, 98, 96]},
    {"name": "Abhishek", "marks": [99, 98, 97]},
    {"name": "Ankesh", "marks": [89, 88, 87]},
    {"name": "Ashok", "marks": [85, 87, 84]},
    {"name": "Vipgu", "marks": [87, 84, 83]}
]

# Display each student's results
for student in students:
    marks = student["marks"]

    total_marks = sum(marks)
    average_marks = total_marks / len(marks)
    highest_marks = max(marks)
    lowest_marks = min(marks)

    print(f"\nStudent name: {student['name']}")
    print(f"Total marks: {total_marks}")
    print(f"Average marks: {average_marks:.2f}")
    print(f"Highest marks: {highest_marks}")
    print(f"Lowest marks: {lowest_marks}")

# Find the class topper
topper = max(
    students,
    key=lambda student: sum(student["marks"]) / len(student["marks"])
)

print(f"\nClass topper: {topper['name']}")
print(
    f"Topper's average: "
    f"{sum(topper['marks']) / len(topper['marks']):.2f}"
)