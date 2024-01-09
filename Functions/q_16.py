def square1():
    lst = []
    for i in range(1, 31):
        lst.append(i ** 2)
    print(lst)


def square2():
    print([i ** 2 for i in range(1, 31)])


square1()
square2()
