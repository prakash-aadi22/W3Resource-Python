def pattern():
    for i in range(1, 11):
        for j in range(1, i):
            print(j, end="")
        print()
    print("\n=================================")
    for a in range(10):
        print(str(a) * a)
    print("\n=================================")
    for i in range(1, 11):
        for j in range(1, 10 - i + 1):
            print(j, end="")
        print()
    print("------------------------------------")
    for i in range(9, 0, -1):
        for j in range(1, i + 1):
            print(j, end="")
        print()
    print("\n=================================")
    for a in range(9, 0, -1):
        print(str(a) * a)


pattern()
