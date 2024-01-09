def first_three(s):
    if len(s) > 3:
        return s[:3]
    elif len(s) == 3:
        return s
    return "Length less than 3."


print(first_three('ipy'))
print(first_three('python'))
print(first_three('py'))
