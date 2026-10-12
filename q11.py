#  Sanika Patil

subjects = ["Maths", "Science"]

subjects.append("English")
subjects.insert(1, "Hindi")
subjects.extend(["Art", "Music"])
subjects.remove("Art")

popped = subjects.pop()
print(f"Popped: {popped}")

subjects.sort()

print(subjects, len(subjects))
print(f"Hindi index: {subjects.index('Hindi')}")