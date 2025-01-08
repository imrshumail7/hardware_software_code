Python 3.13.1 (v3.13.1:06714517797, Dec  3 2024, 14:00:22) [Clang 15.0.0 (clang-1500.3.9.4)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> def main():
...     name = "Professor Nedd"
...     print("we want to know if you like programming!")
...     print()
...     print("Do you like programming{}?. format(name))
...           
SyntaxError: unterminated string literal (detected at line 5)
>>> def main():
...     name = "Professor Nedd"
...     print("we want to know if you like programming!")
...     print()
...     print("Do you like programming{}".format(name))
...     answer = input()
...     print("Great! You said {}?".format(answer))
...     print("Let's start learning some Python today")
... 
...     
>>> if __name__ == "__main__":
...     main()
