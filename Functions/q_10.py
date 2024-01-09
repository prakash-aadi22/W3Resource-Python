def check_even(lst):
    even_list = []
    for i in lst:
        if i % 2 == 0:
            even_list.append(i)
    print(even_list)


check_even([1, 2, 3, 4, 5, 6, 7, 8, 9])
