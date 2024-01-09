from functools import reduce
from operator import mul


def multiply_list(lst):
    print(reduce(mul, lst))


def multiply_list1(lst):
    ans = 1
    for i in lst:
        ans *= i
    print(ans)


multiply_list([1, 2, -8])
multiply_list1([1, 2, -8])
