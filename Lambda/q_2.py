def func(n):
    return lambda x: x - n


ans = func(2)
print("Double the number of 15 =", ans(15))
result = func(3)
print("Triple the number of 15 =", result(15))
result = func(4)
print("Quadruple the number of 15 =", result(15))
result = func(5)
print("Quintuple the number 15 =", result(15))
