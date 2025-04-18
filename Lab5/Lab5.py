def menu():
    # Decoding menu
    print("\nDecoding Menu")
    print("-------------")
    print("1. Decode hexadecimal")
    print("2. Decode binary")
    print("3. Convert binary to hexadecimal")
    print("4. Quit")

    choice = input("Please enter an option: ")  # Enter 1-4 only
    return choice


def main():
    while True:
        option = menu()  # Display the menu

        if option == '1':
            hex_input = input("Please enter the numeric string to convert: ")
            if (hex_input[1] == 'x') or (hex_input[1] == 'X'):
                hex_input = hex_input[2:]
            try:
                result = hex_string_decode(hex_input)
                print(f"Result: {result}\n")  # Add newline for formatting
            except ValueError as e:
                print(e)
        elif option == '2':  # If user chooses to decode binary
            binary_input = input("Please enter the numeric string to convert: ")  # Get input
            try:
                result = binary_string_decode(binary_input)  # Decode the binary string
                print(f"Result: {result}\n")  # Add newline for formatting
            except ValueError as e:
                print(e)
        elif option == '3':  # If user chooses to convert binary to hexadecimal
            binary_input = input("Please enter the numeric string to convert: ")  # Get input
            if (binary_input[1] == 'x') or (binary_input[1] == 'X'):
                binary_input = binary_input[2:]
            try:
                result = binary_to_hex(binary_input)  # Convert the binary string to hexadecimal

                # Manually get the result with leading zeros to ensure it is 4 characters long
                if len(result) < 4:
                    result = '0' * (4 - len(result)) + result

                print(f"Result: {result}\n")  # Add newline
            except ValueError as e:
                print(e)
        elif option == '4':
            print("Goodbye!")
            break  # Exit



def hex_char_decode(a):
    # Decodes a single hexadecimal digit and returns its value.

    if a.isdigit():  # Check if the digit is 0-9
        return int(a)  # return int only
    elif a in 'abcdef':
        return 10 + ('abcdef'.index(a))  # Convert since 10
    elif a in 'ABCDEF':
        return 10 + ('ABCDEF'.index(a))  # Both upper and lowercase

    else:
        raise ValueError("Invalid hexadecimal digit") # not needed for the autograder


def hex_string_decode(hex_string):
    # Decodes an entire hexadecimal string and returns its value.
    # Remove the '0x' (as required in lab...) prefix if it exists
    if len(hex_string) >= 2 and hex_string[0] == '0' and hex_string[1] == 'x':
        hex_string = hex_string[2:]  # Use the list
    total = 0  # Initialize total to 0
    # Iterate over each character in the hexadecimal string
    for i in hex_string:
        # Keep multiplying by 16 and adding the value of the character
        total = total * 16 + hex_char_decode(i)
    return total  # Return the final decimal value


def binary_string_decode(binary_string):
    # Decodes a binary string and returns its value.
    # Remove the '0b' prefix if it exists
    if len(binary_string) >= 2 and binary_string[0].lower() == '0' and binary_string[1].lower() == 'b':
        binary_string = binary_string[2:]  # Strip off the prefix
    total = 0  # Initialize total to 0
    # Iterate over each character in the binary string
    for j in binary_string:
        # Check if the character is a valid binary digit (0 or 1)
        if j not in '01':
            raise ValueError("Invalid binary digit")  # Raise an error if invalid
        # Keep adding the integer value of the character
        total = total * 2 + int(j)
    return total  # Return the  decimal value


def binary_to_hex(binary):
    # Binary to hexadecimal
    # Convert the binary string to a decimal first
    decimal = binary_string_decode(binary)  # call previous function
    hex_string = ""  # Set up an empty string we are using later
    # Handle the case where the decimal value is zero
    if decimal == 0:
        return "0"  # Return "0" for zero
    # Convert the decimal value to hexadecimal
    while decimal > 0:
        # Get the remainder when divided by 16 (for hex digit)
        remainder = decimal % 16
        # Convert remainder to a hexadecimal character
        if remainder < 10:
            hex_string = str(remainder) + hex_string  # Numeric characters (0-9)
        else:
            hex_string = 'ABCDEF'[remainder - 10] + hex_string  # Uppercase letters (A-F)

        decimal //= 16  # Divide the decimal value by 16
    return hex_string  # Return the hex value


if __name__ == "__main__":
    main()  # Call the main function to run the program
