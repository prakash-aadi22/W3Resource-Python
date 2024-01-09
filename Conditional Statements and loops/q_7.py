def p(lst):
    for item in lst:
        print("Type of", item, "is", type(item))


data_list = [1452, 11.23, 1 + 2j, True, 'w3resource', (0, -1), [5, 12], {"class": 'V', "section": 'A'}]
p(data_list)
