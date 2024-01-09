def add():
    ans = 0
    for i in dic.values():
        ans += i
    print(ans)
    print(sum(dic.values()))


dic = {'data1': 10, 'data2': -5, 'data3': 2}
add()
