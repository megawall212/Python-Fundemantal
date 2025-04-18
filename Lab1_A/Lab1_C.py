#Write a program named Lab1_C.py that will calculate the number of days between 2 dates.

year_date1 =int(input("Enter the year for date 1: "))
month_date1 =int(input("Enter the month for date 1: "))
day_date1 =int(input("Enter the day for date 1: "))
year_date2 =int(input("Enter the year for date 2: "))
month_date2 =int(input("Enter the month for date 2: "))
day_year2 =int(input("Enter the day for date 2: "))

year_difference= year_date2-year_date1
month_difference = month_date2-month_date1
day_difference =day_year2-day_date1

convert1 = 360 * year_difference
convert2 = 30 * month_difference
convert3 = day_difference

final_difference=abs(convert1+convert2+convert3)
print(f'The difference between {month_date1}/{day_date1}/{year_date1} and {month_date2}/{day_year2}/{year_date2} is {final_difference} days!')