#SANIKA PATIL

# marks = [67, 89, 45, 92, 78, 56, 81, 73]. 
# Print the number of students, the highest, the lowest, the total, the average (2 decimal places) 
# and the marks sorted from highest to lowest (use sorted() with reverse=True).

marks = [67, 89, 45, 92, 78, 56, 81, 73]

students = len(marks)
highest = max(marks)
lowest = min(marks)
total = sum(marks)
average = total / students
sorted_marks = sorted(marks, reverse=True)

print(f"Students: {students}")
print(f"Highest: {highest}")
print(f"Lowest: {lowest}")
print(f"Total: {total}")
print(f"Average: {average:.2f}")
print(f"Sorted: {sorted_marks}")