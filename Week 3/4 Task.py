# def gcd(a, b):
#     while b:
#         a, b = b, a % b
#     return a

# A, B = 2, 3
# C, D = 4, 5
# num = A * D
# den = B * C

# g = gcd(num, den)
# print(f"Result: {num//g}/{den//g}")

def inside_circle(x, y, a, b, r):
    return (x - a)**2 + (y - b)**2 <= r*r

points = [(1,2), (3,3), (5,5)]
count = 0

for p in points:
    if inside_circle(p[0], p[1], 0, 0, 5):
        count += 1

print("Points inside:", count)
