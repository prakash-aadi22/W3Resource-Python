def check_prime(n):
    flag = False
    if n == 0 or n == 1:
        print(n, "is not prime number.")
    else:
        for i in range(2, n):
            if n % i == 0:
                flag = True
        if flag:
            print(n, "is not prime number.")
        else:
            print(n, "is a prime number.")


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def print_prime(n):
    prime = []
    not_prime = []
    print("Prime numbers up to", n, "are:")
    for i in range(2, n + 1):
        if is_prime(i):
            prime.append(i)
        else:
            not_prime.append(i)
    print(prime)
    print(not_prime)


check_prime(9)

# for j in range(101):
#     check_prime(j)

print_prime(101)
