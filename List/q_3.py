def largest(lst):
    max_value = lst[0]
    for i in lst:
        if i > max_value:
            max_value = i
    print(max_value)


def largest1(lst):
    print(max(lst))


largest([1, 0, -8, 9, 2, 7, 3])
largest1([1, 0, -8, 9, 2, 7, 3])
