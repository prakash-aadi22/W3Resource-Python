def histogram(nums):
    for j in nums:
        print("@" * j)


histogram([2, 3, 6, 5])
n = int(input("Enter the length of the list: "))
lst = []
for i in range(n):
    lst.append(int(input("Enter the value of " + str(i) + "th index: ")))

histogram(lst)
