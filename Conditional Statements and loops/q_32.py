def check(c):
    if c.lower() in ('a', 'e', 'i', 'o', 'u'):
        print(c + " is vowel.")
    else:
        print(c + " is a consonant.")


check(input("Enter a letter: "))
