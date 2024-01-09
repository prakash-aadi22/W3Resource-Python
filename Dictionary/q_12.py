def remove():
    if 'a' in dic:
        del dic['a']
    print(dic)


dic = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
remove()
