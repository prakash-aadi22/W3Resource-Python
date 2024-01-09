def area(b, h):
    return (b * h) / 2


base = float(input("Base of triangle: "))
height = float(input("Height of triangle: "))
print("Area of the triangle: " + str(area(base, height)))
