add = lambda x: x + 15
mul = lambda x, y: x * y
print(add(10))
print(mul(12, 4))

print((lambda x: x + 15)(10))

print((lambda x, y: x * y)(12, 4))


def add1():
    return lambda a: a + 15


def mul1():
    return lambda m, n: m * n


ans = add1()
print(ans(10))
ans1 = mul1()
print(ans1(12, 4))
