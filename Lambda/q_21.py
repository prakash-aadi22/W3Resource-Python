def mul_list(n):
    return lambda lst: [x * n for x in num]


num = [2, 4, 6, 9, 11]
ans = mul_list(2)
print(ans(num))
