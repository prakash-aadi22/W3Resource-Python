bases_num = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
index = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list(map(pow, bases_num, index)))
print(list(map(lambda x, y: x ** y, bases_num, index)))
