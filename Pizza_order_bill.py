'''
PIZZA ORDER PRACTICE
Congratulations, you've got a job at Python Pizza! Your first job is to build an automatic pizza order program.
Based on a user's order, work out their final bill.
Small pizza (S): $15
Medium pizza (M): $20
Large pizza (L): $25
Add pepperoni for small pizza (Y or N): +$2
Add pepperoni for medium or large pizza (Y or N): +$3
Add extra cheese for any size pizza (Y or N): +$1
'''

print("Thank you for choosing Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L: ") # What size pizza do you want? S, M, or L
add_pepperoni = input("Do you want pepperoni? Y or N: ") # Do you want pepperoni? Y or N
extra_cheese = input("Do you want extra cheese? Y or N: ") # Do you want extra cheese? Y or N
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
total_bill_amt = 0
if size.upper() == "S":
    total_bill_amt += 15
elif size.upper() == "M":
    total_bill_amt += 20
elif size.upper() == "L":
    total_bill_amt += 25

if add_pepperoni.upper() == "Y" and size.upper() == "S":
    total_bill_amt += 2
elif add_pepperoni.upper() == "Y" and  size.upper() in ("M", "L"):
    total_bill_amt += 3

if extra_cheese.upper() == "Y":
    total_bill_amt +=1

print(f"Total bill amount is ${total_bill_amt}")
