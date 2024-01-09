# def value(x):
#     try:
#         int_value = int(input(x))
#         return int_value
#     except ValueError:
#         print("Error: Invalid input, input a valid integer.")
#
#
# n = value("Enter a number: ")
# print("Input value: ", n)

def value(x):
    try:
        print("Input value:", int(x))
    except ValueError:
        print("Error: Invalid input, input a valid integer.")


value(input("Enter a number: "))
