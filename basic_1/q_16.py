def difference(n):
    if n <= 17:
        return 17 - n
    else:
        return (n - 17) * 2


n = int(input("Enter a number: "))
if n > 17:
    print(abs(n - 17) * 2)
else:
    print(abs(n - 17))

print(difference(n))
