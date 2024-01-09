def triangle_check(a, b, c):
    if a == b == c:
        return "Equilateral Triangle"
    elif a != b and a != c and b != c:
        return "Scalene Triangle"
    else:
        return "Isosceles Triangle"


def triangle_check1(a, b, c):
    if a == b == c:
        return "Equilateral Triangle"
    elif a == b or a == c or b == c:
        return "Isosceles Triangle"
    else:
        return "Scalene Triangle"


x = (int(input("Enter the length of first side of the triangle: ")))
y = (int(input("Enter the length of second side of the triangle: ")))
z = (int(input("Enter the length of third side of the triangle: ")))
print(triangle_check(x, y, z))
print(triangle_check1(x, y, z))
