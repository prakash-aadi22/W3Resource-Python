def intersection1():
    lst = []
    for x in l1:
        if x in l2 and x not in lst:
            lst.append(x)
    return lst


def intersection2():
    return sorted(list(set(l1).intersection(set(l2))))


def intersection3():
    return list(filter(lambda x: x in l1, l2))


def intersection4():
    return lambda lst: list(filter(lambda x: x in l1 and x in l2 and x not in lst, l1))


l1 = [1, 2, 3, 5, 7, 8, 9, 10]
l2 = [1, 2, 4, 8, 9]

print(intersection1())
print(intersection2())
print(intersection3())
ans = intersection4()
print(ans([]))
