#SANIKA PATIL
    
maths = int(input("enter maths marks:")) 
science = int(input("enter science marks:")) 
english = int(input("enter english marks:")) 

total = maths + science + english
percentage = (total/300)*100

print(f"maths: {maths}")
print(f"science: {science}")
print(f"english: {english}")
print(f"total: {total}")
print(f"percentage: {percentage:2f}")