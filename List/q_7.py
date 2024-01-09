def remove_duplicate(lst):
    lst1 = []
    for i in lst:
        if i not in lst1:
            lst1.append(i)
    print(lst1)


def remove_duplicate1(lst):
    print(sorted(list(set(lst))))


remove_duplicate([10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40])
remove_duplicate1([10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40])
