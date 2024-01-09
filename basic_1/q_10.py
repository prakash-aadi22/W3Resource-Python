n = int(input("Enter the number: "))
print(n + (n * n) + (n * n * n))

n1 = int("%s" % n)
n2 = int("%s%s" % (n, n))
n3 = int("%s%s%s" % (n, n, n))

print(n1 + n2 + n3)
