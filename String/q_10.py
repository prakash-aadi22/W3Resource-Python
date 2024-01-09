def change(s):
    # return s[-1:] + s[1:-1] + s[:1]
    return s[-1] + s[1:-1] + s[0]


print(change("Hello"))
print(change("abcd"))
print(change("12345"))
