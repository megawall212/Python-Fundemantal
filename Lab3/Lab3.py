import math
#Set up the global variables

current_result = 0.0
total_sum = 0.0
num_calculations = 0


def whattoinput (float_input):
    # Get a float input
    while True:
        try:
            return float(input(float_input))
        except ValueError:
            print("Error: invalid input! Please enter a valid number.")


def calculate(option):
    #What's wrong with global variables?
    global current_result, total_sum, num_calculations
    if option in [1, 2, 3, 4, 5, 6]:
        first_operand = whattoinput("Enter first operand: ")
        second_operand = whattoinput("Enter second operand: ")

        if option == 1:  # 1.Addition
            current_result = first_operand + second_operand
        elif option == 2:  # 2.Subtraction
            current_result = first_operand - second_operand
        elif option == 3:  # 3.Multiplication
            current_result = first_operand * second_operand
        elif option == 4:  # 4.Division
            if second_operand == 0:
                print("Error: Division by zero!")
                return False
            current_result = first_operand / second_operand
        elif option == 5:  # 5.Exponentiation
            current_result = first_operand ** second_operand
        elif option == 6:  # 6.Logarithm
            if first_operand <= 0 or second_operand <= 0:
                print("Error: Logarithm base and operand must be positive!")
                return False
            current_result = math.log(second_operand, first_operand)

        total_sum += current_result
        num_calculations += 1
        #print("Current Result: {:.2f}".format(current_result))
        return True

    elif option == 7:  # 7.Display Average
        if num_calculations == 0:
            print("Error: No calculations yet to average!")
        else:
            average = total_sum / num_calculations
            print(f"Sum of calculations: {total_sum:.2f}")
            print(f"Number of calculations: {num_calculations}")
            print(f"Average of calculations: {average:.2f}")
        return True

    else:
        print("Error: Invalid selection!")
        return False


def menu():

    print(f'Current Result: {current_result}')
    print("\nCalculator Menu")
    print("---------------")
    print("0. Exit Program")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exponentiation")
    print("6. Logarithm")
    print("7. Display Average")


def main():

    global current_result
    menu()  # Call menu function
    run = True
    while run:
        try:
            selection = int(input("Enter Menu Selection: "))

            if selection == 0:
                print("Thanks for using this calculator. Goodbye!")
                run = False
                break

            elif 1 <= selection <= 7:
                if calculate(selection):
                    if selection == 7:
                        # Keep working
                        continue
                    else:
                        # Go back to menu
                        menu()
            else:
                print("Error: Invalid selection!")

        except ValueError:
            print("Error: Invalid selection!")


if __name__ == "__main__":
    main()
