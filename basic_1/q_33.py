def sum_three(a, b, c):
    if a == b or b == c or a == c:
        return 0
    else:
        return a + b + c


print(sum_three(2, 1, 2))
print(sum_three(3, 2, 2))
print(sum_three(2, 2, 2))
print(sum_three(1, 2, 3))
x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))
z = int(input("Enter the third number: "))
print(sum_three(x, y, z))
