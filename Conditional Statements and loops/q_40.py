import statistics


def find_median(x, y, z):
    lst = [x, y, z]
    print(statistics.median(lst))

    m = sorted([x, y, z])
    print(m[1])


find_median(int(input("Enter the first number: ")), int(input("Enter the second number: ")),
            int(input("Enter the third number: ")))
