def add_avg(list1):
    add = 0.0
    for i in list1:
        add += i
    print("Sum of the all number is: " + str(add))
    print("Average of the all numbers is: " + str(add / len(list1)))


lst = []
num = count = 0
print("Input some integers to calculate their sum and average. Input -1 to exit.")
while num != -1:
    num = int(input("Enter the number: "))
    if num != -1:
        lst.append(num)
        count += 1
add_avg(lst)
