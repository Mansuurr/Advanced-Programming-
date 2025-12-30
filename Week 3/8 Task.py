# n = int(input("Enter n: "))

# for i in range(1, n+1):
#     digits = str(i)
#     ok = True
#     for d in digits:
#         if d == '0' or i % int(d) != 0:
#             ok = False
#     if ok:
#         print(i, end=" ")

m = int(input("Enter length: "))
A = []

for i in range(m):
    A.append(int(input()))

print("Original:", A)

if m > 1:
    A[0], A[-1] = A[-1], A[0]

print("Result:", A)
