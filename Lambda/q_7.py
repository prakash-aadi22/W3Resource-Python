def check(x):
    return lambda s: s[0] == x


def check1():
    return lambda s: True if s.startswith('a') else False


ans = check('a')
print(ans("ans"))
ans = check('a')
print(ans("sna"))
print("==========")
ans = check1()
print(ans("ans"))
ans = check1()
print(ans("sna"))
print("==========")

starts_with = lambda x: True if x.startswith('P') else False
print(starts_with('Python'))
print(starts_with('Java'))
