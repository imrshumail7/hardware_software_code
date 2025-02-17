def main():
    print("Welcome! This program allows you to add two whole numbers repeatedly until you choose to exit.")

    while True:
        try:
            num1 = int(input("Enter the first whole number: "))
            num2 = int(input("Enter the second whole number: "))
            print(f"The sum of {num1} and {num2} is {num1 + num2}")
        except ValueError:
            print("Invalid input. Please enter whole numbers only.")
            continue

        exit_program = input("Would you like to exit? (yes/no): ").strip().lower()
        if exit_program == 'yes':
            print("Thank you for using the program! Goodbye.")
            break

if __name__ == "__main__":
    main()
