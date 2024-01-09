def sum_list(lst):
    print(sum(lst))


def sum_list1(lst):
    ans = 0
    for i in lst:
        ans += i
    print(ans)


def sum_list2(lst):
    print(sum(i for i in lst))


sum_list([1, 2, -8])
sum_list([1, 2, 8])

sum_list1([1, 2, -8])
sum_list1([1, 2, 8])

sum_list2([1, 2, -8])
sum_list2([1, 2, 8])
