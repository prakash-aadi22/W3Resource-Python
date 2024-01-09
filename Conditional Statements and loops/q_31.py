def age(human_year):
    if human_year < 0:
        print("Age must be a positive number.")
        exit()
    elif human_year <= 2:
        return human_year * 10.5
    else:
        return ((human_year - 2) * 4) + (10.5 * 2)


x = age(int(input("Enter the dog's age in human years: ")))
print("The dog's age in dog's years is: ", int(x))
for i in range(10, 0, -1):
    print("The dog's age in dog's years for human year ", i, " is: ", int(age(i)))
