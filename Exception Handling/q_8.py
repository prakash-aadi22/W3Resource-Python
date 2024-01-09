def div(x, y):
    try:
        print(x, "/", y, "=", int(x / y))
    except ArithmeticError:
        print("Error: Arithmetic error occurred!")


div(100, 20)
div(100, 0)
