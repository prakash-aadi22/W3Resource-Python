def removing(lst):
    for (i, x) in enumerate(lst):
        if i != 0 and i != 4 and i != 5:
            print(x, end=", ")
    print()
    print([x for (i, x) in enumerate(lst) if i not in (0, 4, 5)])


removing(['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow'])
