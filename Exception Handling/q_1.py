def div(x, y):
    try:
        print(x, "/", y, "=", int(x / y))
    except ZeroDivisionError:
        print("The division by zero operation is not allowed.")


div(100, 20)
div(100, 0)
