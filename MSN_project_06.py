def introduction():
    print("Welcome to the Number Converter!")
    print("This program converts numbers between decimal and binary.")
    print("You can also convert numbers to hexadecimal and octal for bonus points.")
    print("The program will continue running until you decide to exit.\n")

def decimal_to_binary():
    while True:
        try:
            decimal = int(input("Enter a decimal number: "))
            if decimal < 0:
                print("Please enter a non-negative integer.")
                continue
            print(f"Binary equivalent: {bin(decimal)[2:]}\n")
            break
        except ValueError:
            print("Invalid input. Please enter a valid decimal number.\n")

def binary_to_decimal():
    while True:
        binary = input("Enter a binary number: ")
        if all(bit in '01' for bit in binary):
            print(f"Decimal equivalent: {int(binary, 2)}\n")
            break
        else:
            print("Invalid input. Please enter a valid binary number.\n")

def decimal_to_hex_octal():
    while True:
        try:
            decimal = int(input("Enter a decimal number for hex and octal conversion: "))
            if decimal < 0:
                print("Please enter a non-negative integer.")
                continue
            print(f"Hexadecimal equivalent: {hex(decimal)[2:].upper()}")
            print(f"Octal equivalent: {oct(decimal)[2:]}\n")
            break
        except ValueError:
            print("Invalid input. Please enter a valid decimal number.\n")

def main():
    introduction()

    while True:
        print("Choose an option:")
        print("1. Convert Decimal to Binary")
        print("2. Convert Binary to Decimal")
        print("3. Convert Decimal to Hex and Octal (Bonus)")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            decimal_to_binary()
        elif choice == "2":
            binary_to_decimal()
        elif choice == "3":
            decimal_to_hex_octal()
        elif choice == "4":
            print("Thank you for using the Number Converter. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option (1-4).\n")

if __name__ == "__main__":
    main()
