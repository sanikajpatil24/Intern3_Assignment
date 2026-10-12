#SANIKA PATIL

maths = int(input("enter maths marks : "))
science = int(input("enter science marks : "))

passed_maths = maths >=35
passed_science = science >=35

passed_both = passed_maths and passed_science
reexam = (not passed_maths) or (not passed_science)

print(f"maths :{maths}")
print(f"science :{science}")
print(f"Passed maths : {passed_maths}")
print(f"Passed science : {passed_science}")
print(f"Passed both : {passed_both}")
print(f"Reexam : {reexam}")