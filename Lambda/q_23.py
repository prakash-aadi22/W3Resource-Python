def add_positive():
    return lambda lst: sum(x for x in num if x > 0)


def add_negative():
    return lambda lst: sum(x for x in num if x < 0)


num = [2, 4, -6, -9, 11, -12, 14, -5, 17]
ans1 = add_positive()
print(ans1(num))
ans2 = add_negative()
print(ans2(num))
