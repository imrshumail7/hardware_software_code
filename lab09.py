def print_lyrics():
    print("I'm a programmer, and I'm okay.")
    print("I code all night, and I code all day.")


def repeat_lyrics(count = 1):
    for number in range(count):
        print_lyrics()
        print("############")


def main():
    repeat_lyrics()
    repeat_lyrics(4)


if __name__ == "__main__":
    main()


I'm a programmer, and I'm okay.
I code all night, and I code all day.
############
I'm a programmer, and I'm okay.
I code all night, and I code all day.
############
I'm a programmer, and I'm okay.
I code all night, and I code all day.
############
I'm a programmer, and I'm okay.
I code all night, and I code all day.
############
I'm a programmer, and I'm okay.
I code all night, and I code all day.
############
>>> def print_lyrics():
...     print("I'm aprogrammer, and I'm okay.")
...     print("I code all night, and I code all day.")
...
...
>>> def repeat_lyrics(count=1):
...     for number in range(count):
...         print("{}############".format(number),end=".")
...         print_lyrics()
...         print("############")
...
...
>>> def main():
...     repeat_lyrics()
...     repeat_lyrics(4)
...
...
>>> if __name__ == "__main__":
...     main()
...
...
0############.I'm aprogrammer, and I'm okay.
I code all night, and I code all day.
############
0############.I'm aprogrammer, and I'm okay.
I code all night, and I code all day.
############
1############.I'm aprogrammer, and I'm okay.
I code all night, and I code all day.
############
2############.I'm aprogrammer, and I'm okay.
I code all night, and I code all day.
############
3############.I'm aprogrammer, and I'm okay.
I code all night, and I code all day.
############
