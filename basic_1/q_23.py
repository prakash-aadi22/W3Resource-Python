def copies(s, n):
    if len(s) <= 2:
        return s * n
    else:
        return s[:2] * n + s[2:]


print(copies(input("String: "), int(input("Integer: "))))
