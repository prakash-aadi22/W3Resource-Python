def common(lst1, lst2):
    ans = False
    for i in lst1:
        for j in lst2:
            if i == j:
                ans = True
    return ans


print(common([1, 2, 3, 4, 5], [9, 8, 7, 6, 5]))
print(common([1, 2, 3, 4, 0], [9, 8, 7, 6, 5]))
