def collatz_sequence(n):

    print(n, end=' ')

    # If n is 1, we stop the recursion
    if n == 1:
        return

    # If n is even, call the function with n divided by 2
    if n % 2 == 0:
        collatz_sequence(n // 2)
    # If n is odd, call the function with 3n + 1
    else:
        collatz_sequence(3 * n + 1)


def print_backwards(s):
    # If the string is empty, we stop
    if s == "":
        return

    # Print the last character of the string
    print(s[-1], end='')

    # Call the function again with the string excluding the last character
    print_backwards(s[:-1])


def hammer_profit(cost, prices):
    #If the prices list is empty, return 0
    if not prices:
        return 0

    # Calculate profit for the first price
    profit = prices[0] - cost

    # return the accumulated profits (both positive and negative)

    return profit + hammer_profit(cost, prices[1:])



def format_names(names):
    # If there are no names left, return an empty list
    if not names:
        return []

    current_name = names[0]  # Get the current name
    # Check if the name is already in the correct format
    if ',' in current_name:
        formatted_name = current_name  # Keep the name as is
    else:
        # Manually find the space separating first and last names
        space_index = current_name.find(' ')
        if space_index != -1:
            first_name = current_name[:space_index]  # Get first name
            last_name = current_name[space_index + 1:]  # Get last name
            formatted_name = f"{last_name}, {first_name}"  # Format as 'last, first'
        else:
            formatted_name = current_name  # If no space, keep it as it is

    # Recursion: Combine the results
    return [formatted_name] + format_names(names[1:])



def main():
    # Example usage for each problem

    # Problem 1: Collatz Sequence
    print("Collatz Sequence:")

    #collatz_sequence(13)  # Example
    #print("\n")

    # Problem 2: Print Backwards
    print("Print Backwards:")
    #print_backwards("Hello, world!")  # Example
    #print("\n")

    # Problem 3: Hammer Profit
    print("Hammer Profit:")
    #print(hammer_profit(15.00, [14.00, 15.00, 17.00]))  # Output: 1.0
    #print(hammer_profit(20.00, [19.00, 18.00, 23.00, 22.50, 15.00, 25.00]))  # Output: 2.5
    #print("\n")

    # Problem 4: Formatting Customer Names
    print("Format Customer Names:")
    #formatted_names = format_names(["Allen Anderson", "Bruce Baker", "Cook, Claire", "Dunn, David"])
    #print(formatted_names)  # Output the formatted names


# Main
if __name__ == "__main__":
    main()
