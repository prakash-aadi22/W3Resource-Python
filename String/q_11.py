def remove_odd_index(s):
    result = ""
    for i in range(len(s)):
        if i % 2 == 0:
            result = result + s[i]
    print(result)
    return s[0::2]


def remove_even_index(s):
    result = ""
    for i in range(len(s)):
        if i % 2 != 0:
            result = result + s[i]
    print(result)
    return s[1::2]


print(remove_odd_index("Python"))
print(remove_odd_index("Hello"))
print(remove_odd_index("abcdef"))
print("===============")
print(remove_even_index("Python"))
print(remove_even_index("Hello"))
print(remove_even_index("abcdef"))
