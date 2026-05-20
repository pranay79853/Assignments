# Program to calculate customer due amount after paying a bill

# Taking input from the user
bill_amount = float(input("Enter the bill amount: "))
paid_amount = float(input("Enter the amount paid by customer: "))

# Checking payment status
if paid_amount < bill_amount:
    due_amount = bill_amount - paid_amount
    print("Customer Due Amount =", due_amount)

elif paid_amount > bill_amount:
    extra_amount = paid_amount - bill_amount
    print("Extra Amount Paid =", extra_amount)

else:
    print("Bill Paid Successfully. No Due Amount.")