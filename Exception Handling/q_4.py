# def get_numeric_input(prompt):
#     while True:
#         try:
#             value = float(input(prompt))
#             return value
#         except ValueError:
#             print("Error: Invalid input. Please Input a valid number.")
#
#
# n1 = get_numeric_input("Input the first number: ")
# n2 = get_numeric_input("Input the second number: ")
# result = n1 * n2
# print("Product of the said two numbers:", result)


def value(x, y):
    try:
        print("Product of the said two numbers:", int(x) * int(y))
    except ValueError:
        print("Error: Invalid input, input a valid integer.")


a = input("Enter the first number: ")
b = input("Enter the second number: ")
value(a, b)
