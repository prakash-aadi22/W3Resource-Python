def div():
    return lambda lst: [x for x in num if x % 13 == 0 or x % 19 == 0]


num = [19, 65, 57, 39, 152, 639, 121, 44, 90, 190]
ans = div()
print(ans(num))
