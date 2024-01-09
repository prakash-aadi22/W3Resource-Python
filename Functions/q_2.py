def sum1(lst):
    ans = 0
    for i in lst:
        ans += i
    print(ans)


def sum2(lst):
    print(sum(lst))


sum1((8, 2, 3, 0, 7))
sum2((8, 2, 3, 0, 7))
