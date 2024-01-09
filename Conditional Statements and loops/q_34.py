def sum_two_integer(a, b):
    # if a + b >= 15 and a + b < 20:
    # if 15 <= a + b < 20:
    #     print(20)
    # else:
    #     print(a + b)

    add = a + b
    if add in range(15, 20):
        print(20)
    else:
        print(add)


sum_two_integer(int(input("Enter the first integer: ")), int(input("Enter the second integer: ")))
