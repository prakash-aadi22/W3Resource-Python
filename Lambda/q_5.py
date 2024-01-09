def even():
    return lambda lst: [x for x in num if x % 2 == 0]


def odd():
    return lambda lst: [x for x in num if x % 2 != 0]


num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_list = even()
print(even_list(num))
odd_list = odd()
print(odd_list(num))
