#SANIKA PATIL 

annual_fee = float(input())
installments = int(input())

installment_amount = annual_fee / installments
remaining = annual_fee - installment_amount

print(f"Annual fee: {annual_fee:.0f}")
print(f"Installments: {installments}")
print(f"Installment: {installment_amount}")
print(f"Remaining: {remaining}")
