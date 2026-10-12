# Sanika Patil

class_data = {
    "Aman": [78, 82, 90],
    "Sita": [91, 88, 95],
    "Ravi": [56, 64, 70]
}

class_total = 0

for name, marks in class_data.items():
    total = sum(marks)
    average = total / len(marks)

    print(f"{name}: total={total}, average={average:.2f}")

    class_total = class_total + total

print(f"Class total: {class_total}")
print(f"Students: {len(class_data)}")
print(f"Names: {sorted(class_data.keys())}")