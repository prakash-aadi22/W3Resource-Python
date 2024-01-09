def change(s):
    if len(s) > 2:
        if s[-3:] == "ing":
            s = s + "ly"
        else:
            s = s + "ing"
    return s


print(change("a"))
print(change("ab"))
print(change("abc"))
print(change("string"))
print(change("ing"))
print(change("ly"))
