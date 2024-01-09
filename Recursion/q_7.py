def sumSeries(n):
    if n < 1:
        return 0
    else:
        return n + sumSeries(n - 2)


print(sumSeries(6))
print(sumSeries(10))
