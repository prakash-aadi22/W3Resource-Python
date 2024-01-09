def square():
    return lambda lst: [x ** 2 for x in num]


def cube():
    return lambda lst: [x ** 3 for x in num]


num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_list = square()
print(even_list(num))
odd_list = cube()
print(odd_list(num))
