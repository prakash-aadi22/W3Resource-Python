def reverse1(s):
    print(s[::-1])


def reverse2(s):
    s1 = ""
    index = len(s)
    while index > 0:
        s1 += s[index - 1]
        index -= 1
    print(s1)


reverse1("1234abcd")
reverse2("1234abcd")
