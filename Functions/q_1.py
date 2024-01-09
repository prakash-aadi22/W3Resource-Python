def max_three(x, y, z):
    if x > y and x > z:
        print(x)
    elif y > z and y > x:
        print(y)
    else:
        print(z)


max_three(1, 2, 3)
max_three(2, 2, 2)
max_three(14, 5, 6)
max_three(4, 15, 6)
