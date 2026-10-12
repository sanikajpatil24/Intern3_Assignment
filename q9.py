# Sanika Patil

marks = {"Maths": 78, "Science": 85, "English": 69}

marks["Hindi"] = 91
marks["English"] = 74

removed = marks.pop("Science")

print(f"Removed: {removed}")
print(f"Total: {sum(marks.values())}")

for subject, mark in marks.items():
    print(f"{subject}: {mark}")
