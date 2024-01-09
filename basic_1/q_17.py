def near_numb(n):
    return abs(n - 1000) <= 100 or abs(n - 2000) <= 100


# n = int(input("Enter your number: "))
# print(near_numb(n))
print(near_numb(int(input("Enter your number: "))))
