def main():
     print("Welcome to my conversation program")
     print("I will keep asking questions until you type 'exit'.")

     name = input("1. What is your name? ")
     question_count = 0

     questions = [
         "What is your favorite show, {}?",
         "Do you like programming, {}?",
         "What is your favorite sport, {}?"
     ]

     for question in questions:
         answer = input(question.format(name))
         if answer.lower() == "exit":
             break
         question_count += 1

     print(f"Thanks for chatting with me, {name}")
     print(f"You answered {question_count} questions")
if __name__ == '__main__':
    main()
