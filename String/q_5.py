def swap(s1, s2):
    str1 = s2[:2] + s1[2:]
    str2 = s1[:2] + s2[2:]
    return str1 + " " + str2


print(swap("abc", "xyz"))
print(swap("abcde", "uvwxyz"))
