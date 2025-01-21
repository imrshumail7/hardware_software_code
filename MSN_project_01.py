def main():
     print("Hello, I would like to get to know a little about you.")
     print("Please answer a few brief questions.")
     name = input("What is your name? ")
     college = input(f"{name}, What college are you attending? ")
     high_school = input(f"{name}, What high school did you attend? ")
     fun_institution = input(f"{name}, Which institution is more fun? ")
     print(f"\nIt was nice to speak with you, {name}.")
     print(f"You are currently attending {college}.")
     print(f"I learned that your high school's name is {high_school}.")
     print(f"You think {fun_institution} is more fun than {high_school}.")
     print("\nIt was fun getting to know a little about you.")
     print("Let's do this again!")


if __name__ == "__main__":
    main()
