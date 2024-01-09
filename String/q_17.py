def copies(s):
    if len(s) >= 2:
        return s[-2:] * 4


print(copies("Python"))
print(copies("Exercises"))
