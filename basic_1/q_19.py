def check(s):
    if s.startswith("is"):
        return s
    else:
        return "is" + s


print(check(input("Enter your string: ")))
