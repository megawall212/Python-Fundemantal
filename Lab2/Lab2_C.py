#Program C will be an improved version of the temperature converter created in Lab 1.
#It will support converting between Fahrenheit, Celsius, and Kelvin.
#Use the following conversions:

# Get the input for temperature
converted_temperature = 0.0
unitfrom = input("Enter the unit you are converting from: ")
unitto = input("Enter the unit you are converting to: ")
temperature = float(input(f"Enter the temperature in {unitfrom}: "))

# Start converting

if unitfrom == "Fahrenheit":
    if unitto == "Celsius":
        converted_temperature = (temperature - 32) * 5 / 9
    elif unitto == "Kelvin":
        converted_temperature = (temperature - 32) * 5 / 9 + 273.15
    elif unitto == "Fahrenheit":
        converted_temperature = temperature

elif unitfrom == "Celsius":
    if unitto == "Fahrenheit":
        converted_temperature = temperature * 9 / 5 + 32
    elif unitto == "Kelvin":
        converted_temperature = temperature + 273.15
    elif unitto == "Celsius":
        converted_temperature = temperature

elif unitfrom == "Kelvin":
    if unitto == "Fahrenheit":
        converted_temperature = (temperature - 273.15) * 9 / 5 + 32
    elif unitto == "Celsius":
        converted_temperature = temperature - 273.15
    elif unitto == "Kelvin":
        converted_temperature = temperature

# Now it's time:
if converted_temperature !=0:
    print(f"That is {converted_temperature:.1f} degrees {unitto}.")
else:
    print("Invalid conversion.")
