def up_low(s):
    up, low = 0, 0
    for i in s:
        if i.isupper():
            up += 1
        elif i.islower():
            low += 1
    print("Number of Upper case characters:", up)
    print("Number of Lower case Characters:", low)


up_low("The quick Brow Fox.")
