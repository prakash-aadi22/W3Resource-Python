def is_perfect_number(n):
    if n <= 0:
        return False

    add = 0
    for i in range(1, n):
        if n % i == 0:
            add += i

    return add == n


def print_perfect_numbers(end):
    print(f"Perfect numbers up to {end}:")
    for i in range(0, end + 1):
        if is_perfect_number(i):
            print(i)


print_perfect_numbers(10000)
