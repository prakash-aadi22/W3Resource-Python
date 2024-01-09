def sumOfDigits(n):
    # ans = 0
    # while n > 0:
    #     ans += (n % 10)
    #     n /= 10
    # return int(ans)
    return sum(int(digit) for digit in str(n))


print(sumOfDigits(int(input("Enter a positive integer: "))))
