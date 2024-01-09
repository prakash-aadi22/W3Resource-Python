num1 = [1, 2, 3]
num2 = [4, 5, 6]
num3 = [7, 8, 9]
ans = map(lambda x, y, z: x + y + z, num1, num2, num3)
print(list(ans))
