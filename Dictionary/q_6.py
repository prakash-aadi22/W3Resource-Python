def square(n):
    d = dict()
    for i in range(1, n + 1):
        d[i] = i * i
    print(d)


def sq(n):
    print({x: x * x for x in range(1, n + 1)})


square(0)
square(1)
square(2)
square(3)
square(4)
sq(5)
sq(6)
sq(7)
sq(8)
sq(9)
