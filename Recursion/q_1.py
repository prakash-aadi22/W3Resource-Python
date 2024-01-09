def list_sum(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        return lst[0] + list_sum(lst[1:])


print(list_sum([2, 4, 5, 6, 7]))
