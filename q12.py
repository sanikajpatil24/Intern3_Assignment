# Sanika Patil
results = [
    ["Aman", 78, 82],
    ["Sita", 91, 88],
    ["Ravi", 56, 64]
]

print(results[1][2])

results[2][1] = 60
results.append(["Maya", 70, 75])

maths_total = 0

for row in results:
    name = row[0]
    maths = row[1]
    science = row[2]
    total = maths + science

    print(f"{name}: Maths={maths}, Science={science}, Total={total}")
    maths_total = maths_total + maths

print(f"Maths total: {maths_total}")
