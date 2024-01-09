from functools import reduce
from operator import mul


def multiply():
    ans = 1
    for i in dic.values():
        ans *= i
    print(ans)
    ans1 = 1
    for i in dic:
        ans1 *= dic[i]
    print(ans1)
    values = list(dic.values())
    result = reduce(mul, values)
    print(result)


dic = {'data1': 10, 'data2': -5, 'data3': 2}
multiply()
