# Sanika Patil
students = {
    "S101": {"name": "Aman", "class": 9, "marks": 78},
    "S102": {"name": "Sita", "class": 10, "marks": 91},
    "S103": {"name": "Ravi", "class": 9, "marks": 56}
}

print(students["S102"]["marks"])

students["S103"]["marks"] = 62

students["S104"] = {
    "name": "Maya",
    "class": 10,
    "marks": 70
}

total_marks = 0

for student_id, info in students.items():
    print(f"{student_id}: {info['name']}, Class {info['class']}, Marks {info['marks']}")
    total_marks = total_marks + info["marks"]
average = total_marks / len(students)

print(f"Average: {average:.2f}")