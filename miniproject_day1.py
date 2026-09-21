# Make a building blocks of text design for Menu
def lines():
    # Print a solid divider line
    print_row(62)

def print_row(width): #Horizontal
    print ("-" * width)

def calculator_addition():
    while True:
        try:
            # Ask user for both numbers
            first_num = float(input(("Enter First Number: ")))
            second_num = float(input(("Enter Second Number: ")))
            result = first_num + second_num
            print (f"The final output is: {result:.2f}\n")
            break  # got valid numbers, stop asking

        except ValueError:
            # Runs if input couldn't be converted to a number
            print ("Invalid input. Please enter in numbers only.\n")

    # Ask if the user wants to do another addition
    option = str(input("Would you like to calculate again?[Y/N]: "))

    while True:
        if option == 'Y' or option == 'y':
            calculator_addition()  # restart this same calculation
        elif option == 'N' or option == 'n':
            return # return here automatically go back to main menu, avoiding nested loops
        else:
            print ("Invalid input. Please enter Y or N.\n")
            return

def calculator_subraction():
    while True:
        try:
            first_num = float(input(("Enter First Number: ")))
            second_num = float(input(("Enter Second Number: ")))
            # Keeps the order the user typed the numbers in
            result = first_num - second_num
            print (f"The final output is: {result:.2f}\n")
            break

        except ValueError:
            print ("Invalid input. Please enter in numbers only.\n")

    option = str(input("Would you like to calculate again?[Y/N]: "))

    while True:
        if option == 'Y' or option == 'y':
            calculator_subraction()
        elif option == 'N' or option == 'n':
            return
        else:
            print ("Invalid input. Please enter Y or N.\n")
            return

def calculator_multiplication():
    while True:
        try:
            first_num = float(input(("Enter First Number: ")))
            second_num = float(input(("Enter Second Number: ")))
            result = first_num * second_num
            print (f"The final output is: {result:.2f}\n")
            break

        except ValueError:
            print ("Invalid input. Please enter in numbers only.\n")

    option = str(input("Would you like to calculate again?[Y/N]: "))

    while True:
        if option == 'Y' or option == 'y':
            calculator_multiplication()
        elif option == 'N' or option == 'n':
            return
        else:
            print ("Invalid input. Please enter Y or N.\n")
            return

def calculator_division():
    while True:
        try:
            first_num = float(input(("Enter First Number: ")))
            second_num = float(input(("Enter Second Number: ")))
            if second_num == 0:
                # Stop division by zero and ask for numbers again
                print ("Cannot divide by 0.")
                continue
            result = first_num / second_num
            print (f"The final output is: {result:.2f}\n")
            break

        except ValueError:
            print ("Invalid input. Please enter in numbers only.\n")

    option = str(input("Would you like to calculate again?[Y/N]: "))

    while True:
        if option == 'Y' or option == 'y':
            calculator_division()
        elif option == 'N' or option == 'n':
            return
        else:
            print ("Invalid input. Please enter Y or N.\n")
            return

def mini_calculator():
    while True:
        # Show the menu
        lines()
        print ("\n--------------'Welcome To Python Mini Calculator'-------------\n")
        print ("[Option 0.] Addition")
        print ("[Option 1.] Subtraction")
        print ("[Option 2.] Multiplication")
        print ("[Option 3.] Division")
        print ("[Option 4.] To Exit\n")
        lines()

        try:
            option = int(input("Enter your option: "))
        except ValueError:
            # User typed something that isn't a number, show menu again
            print ("Invalid input. Please enter a number.\n")
            continue

        # Run the calculator function that matches the chosen option
        if option == 0:
            calculator_addition()

        elif option == 1:
            calculator_subraction()

        elif option == 2:
            calculator_multiplication()

        elif option == 3:
            calculator_division()

        elif option == 4:
            print ("Goodbye!\n")
            break  # ends the while loop, exits the program

        else:
            print ("Invalid option. Try again.\n")

mini_calculator()  # start the program
