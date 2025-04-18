# Write a program named Lab1_B.py that will calculate the sales tax on a purchased item.
# All outputs should be rounded to two decimal places.
item_price=float(input("Enter the price of the item: "))
tax_percentage=float(input("Enter the sales tax percentage:"))
salestax = item_price*(tax_percentage / 100)

total=item_price+salestax
#Save 1 decimal by using rounded function in python
total_price1= round(total, 2)

print(f" Your total is ${total_price1:.2f}")


