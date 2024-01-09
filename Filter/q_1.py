nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list(map(lambda x: print(x, end=", ") if x % 2 != 0 else None, nums))
print()
print(list(filter(lambda x: x % 2 != 0, nums)))
print(list(map(lambda x: x % 2 != 0, nums)))
