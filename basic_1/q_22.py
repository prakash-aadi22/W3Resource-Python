def count_four(nums):
    count = 0
    for j in nums:
        if j == 4:
            count += 1
    return count


n = int(input("Enter the length of the list: "))
lst = []
for i in range(n):
    # value = int(input("Enter the value of " + str(i) + "th index: "))
    # lst.append(value)
    lst.append(int(input("Enter the value of " + str(i) + "th index: ")))

print(count_four(lst))
