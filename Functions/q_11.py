def perfect_number(n):
    add = 0
    for i in range(1, n):
        if n % i == 0:
            add += i
    if n <= 0:
        print(n, "is not a valid number.")
    elif add == n:
        print(n, "is a perfect number.")
    else:
        print(n, "is not a perfect number.")


perfect_number(0)
perfect_number(6)
perfect_number(100)
