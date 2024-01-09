def check(n):
    if n % 2 == 0:
        return "The number " + str(n) + " is even."
    else:
        return "The number " + str(n) + " is odd."


print(check(int(input("Enter a number: "))))
