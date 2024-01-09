from math import gcd

print("GCD of 12 & 17 =", gcd(12, 17))
print("GCD of 4 & 6 =", gcd(4, 6))
print("GCD of 336 & 360 =", gcd(336, 360))
x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))
print("The Greatest Common Divisor(GCD) is: " + str(gcd(x, y)))
