#Program B will be a program to calculate how much you owe in taxes based on your income.
#You will use the numbers from the 2023 federal tax brackets.
#You can also find a brief explanation of tax bracket calculations on that site.

income = abs(float(input('Enter your total income this year: ')))

tax = 0.00
if income <= 11000:
    tax = income * 0.10
elif income <= 44725:
    tax = (income - 11000) * 0.12 + 1100
elif income <= 95375:
    tax = (income - 44725) * 0.22 + 5147
elif income <= 182100:
    tax = (income - 95375) * 0.24 + 16290
elif income <= 231250:
    tax = (income - 182100) * 0.32 + 37104
elif income <= 578125:
    tax = (income - 231250) * 0.35 + 52832
else:
    tax = (income - 578125) * 0.37 + 174238
    tax = round(tax)


print(f"You owe ${tax:.2f} this year.")
