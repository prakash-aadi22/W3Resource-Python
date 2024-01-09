def find(series):
    count_even, count_odd = 0, 0
    for i in series:
        if i % 2 == 0:
            count_even += 1
        else:
            count_odd += 1
    print("Total number of odd: " + str(count_odd))
    print("Total number of even: " + str(count_even))


lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
find(lst)
