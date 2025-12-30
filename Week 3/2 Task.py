# def triangle_area(a, h):
#     return 0.5 * a * h

# def hexagon_area(a):
#     h = (3 ** 0.5) * a / 2
#     return 6 * triangle_area(a, h)

# print("Hexagon area:", hexagon_area(4))

for i in range(3):
    a = float(input("Enter side a: "))
    b = float(input("Enter side b: "))
    area = a * b
    print("Rectangle area:", area)
