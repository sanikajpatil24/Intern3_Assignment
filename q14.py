#Sanika Patil

marks = [32, 45, 28, 67, 33, 90]
new_marks = []

for mark in marks:
    updated_mark = mark + 5
    print(f"Old: {mark} | New: {updated_mark}")
    new_marks.append(updated_mark)

print(new_marks)
print(f"Total: {sum(new_marks)}")
