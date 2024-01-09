def count(s):
    digits = letters = 0
    for c in s:
        if c.isdigit():
            digits += 1
        elif c.isalpha():
            letters += 1
        else:
            pass
    print("Letters: " + str(letters))
    print("Digits: " + str(digits))


count(input("Enter a string: "))
