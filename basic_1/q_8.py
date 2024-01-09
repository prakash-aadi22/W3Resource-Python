i = int(input("Enter the range of list of the color: "))
color_list = []
for i in range(i):
    value = str(input("Enter the name of " + str(i) + "th color: "))
    color_list.append(value)
print("The name of the color on the list is: " + color_list[0], end='')
print(", and the last name of the color on the list is: " + color_list[len(color_list) - 1])
print("and the last name of the color on the list is: " + color_list[-1])
