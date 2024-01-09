def distinct(lst):
    print(list(set(lst)))


def distinct1(lst):
    new_list = []
    for i in lst:
        if i in new_list:
            pass
        else:
            new_list.append(i)
    print(new_list)


distinct([1, 2, 3, 3, 3, 3, 4, 5])
distinct1([1, 2, 3, 3, 3, 3, 4, 5])
