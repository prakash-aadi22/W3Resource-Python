def convert(s):
    count_upper = 0
    for c in s[:4]:
        # if c.upper() == c:
        if c.isupper():
            count_upper += 1
    if count_upper >= 2:
        return s.upper()
    return s


def convert1(s):
    count_upper = sum(1 for c in s[:4] if c.isupper())
    if count_upper >= 2:
        return s.upper()
    else:
        return s


print(convert('Python'))
print(convert('PyThon'))
print("============")
print(convert1('Python'))
print(convert1('PyThon'))
