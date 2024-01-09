def geometric(n):
    if n < 0:
        return 0
    else:
        return 1 / (pow(2, n)) + geometric(n - 1)


print(geometric(7))
print(geometric(4))
