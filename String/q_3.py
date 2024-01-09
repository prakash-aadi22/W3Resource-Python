def con(s):
    if len(s) < 2:
        return ' '
    # return s[0] + s[1] + s[-2] + s[-1]
    return s[0:2] + s[-2:]


print(con(input("Enter a string: ")))
