def match_words(lst):
    count = 0
    for i in lst:
        if len(i) > 1 and i[0] == i[-1]:
            print(i, end=", ")
            count += 1
    print("\n", count)


match_words(['abc', 'xyz', 'aba', '1221', "hell oh", "a", "ab", "aa"])
