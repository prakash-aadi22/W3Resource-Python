def sum_num(a, b, c):
    ans = a + b + c
    if a == b == c:
        ans *= 3

    return ans


print(sum_num(int(input("a:")), int(input("b:")), int(input("c:"))))
