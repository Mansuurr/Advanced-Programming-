# def circle_area(r):
#     return 3.14 * r * r

# def rectangle_area(a, b):
#     return a * b

# def triangle_area(a, h):
#     return 0.5 * a * h

# print("Circle area:", circle_area(5))
# print("Rectangle area:", rectangle_area(4, 6))
# print("Tiangle arear:", triangle_area(6, 3))

arrays = [
    [1, 2, 3, 4],
    [5, 10, 15],
    [2, 4, 6, 8, 10]]

for arr in arrays:
    s = sum(arr)
    avg = s / len(arr)
    print("Array:", arr)
    print("Sum:", s, "Average:", avg)
