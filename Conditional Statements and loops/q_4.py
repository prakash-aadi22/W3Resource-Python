def pattern(n):
    for i in range(n):
        for j in range(i):
            print('* ', end="")
        print('')
    for i in range(n, 0, -1):
        for j in range(i):
            print('* ', end="")
        print('')
    # if i <= n:
    #     print('* ' * i)
    # else:
    #     print('* ' * (2 * n - i))


pattern(int(input("Enter a number: ")))
