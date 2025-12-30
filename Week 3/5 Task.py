# def gcd(a, b):
#     while b:
#         a, b = b, a % b
#     return a

# A, B = 5, 6
# C, D = 1, 3
# num = A*D - C*B
# den = B*D

# g = gcd(abs(num), den)
# print(f"{num//g}/{den//g}")

n = int(input("Enter number: "))
for i in range(1, n+1):
    if n % i == 0:
        print(i, end=" ")
