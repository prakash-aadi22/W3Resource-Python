def smallest(lst):
    min_value = lst[0]
    for i in lst:
        if i < min_value:
            min_value = i
    print(min_value)


def smallest1(lst):
    print(min(lst))


smallest([1, 0, -8, 9, 2, 7, 3])
smallest1([1, 0, -8, 9, 2, 7, 3])
