# import math

# def hypotenuse(a, b):
#     return math.sqrt(a*a + b*b)

# h1 = hypotenuse(3, 4)
# h2 = hypotenuse(6, 8)

# print("Hypotenuse 1:", h1)
# print("Hypotenuse 2:", h2)

# if h1 > h2:
#     print("First is larger")
# else:
#     print("Second is larger")

text = input("Enter string: ")
words = text.split()

result = []
for w in words:
    result.append("".join(sorted(w)))

print(" ".join(result))
