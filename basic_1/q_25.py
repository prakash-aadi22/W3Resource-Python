def check(nums, a):
    return a in nums


print(check([1, 5, 8, 3], 3))
print(check([5, 8, 3], -1))
n = int(input("Enter the length of the list: "))
lst = []
for i in range(n):
    lst.append(int(input("Enter the value of " + str(i) + "th index: ")))

x = int(input("Enter the number to find: "))
print(check(lst, x))
