def identical_digits(num):
    if num < 10 or num > 90:
        raise ValueError("Input must be an integer in the range of 10 to 90.")

    while True:
        print(num)  # Print the current number
        # Extract the digits
        tens = num // 10
        units = num % 10

        # Check if the digits are identical
        if tens == units:
            break  # Exit the loop if digits are identical

        num += 1  # Increment the number


# Example usage:
identical_digits(10)
