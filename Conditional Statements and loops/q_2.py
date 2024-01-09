def temp(n):
    degree = int(n[:-1])
    si_unit = n[-1]
    if si_unit.upper() == 'C':
        print(str(int(round((9 * degree) / 5 + 32))) + " Fahrenheit")
    elif si_unit.upper() == 'F':
        print(str(int(round((degree - 32) * 5 / 9))) + " Celsius")
    else:
        print("Input proper convention.")


x = input("Enter the temperature: ")
temp(x)
