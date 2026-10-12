#SANIKA PATIL

monday = {"Aman", "Sita", "Ravi", "Isha", "Dev"}
tuesday = {"Sita", "Ravi", "Maya", "Dev", "Karan"}

both_days = monday & tuesday
at_least_one = monday | tuesday
monday_only = monday - tuesday
exactly_one = monday ^ tuesday

print(f"Both days: {sorted(both_days)}")
print(f"At least one day: {sorted(at_least_one)}")
print(f"Monday only: {sorted(monday_only)}")
print(f"Exactly one day: {sorted(exactly_one)}")
print(f"Unique students: {len(at_least_one)}")
