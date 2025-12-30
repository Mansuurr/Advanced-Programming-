# def gcd(a, b):
#     while b:
#         a, b = b, a % b
#     return a

# A, B = 12, 18
# g = gcd(A, B)
# lcm = (A * B) // g

# print("GCD:", g)
# print("LCM:", lcm)

import math

a, b, c, d, diag = 5, 6, 7, 8, 9
s1 = (a + b + diag) / 2
s2 = (c + d + diag) / 2

area = math.sqrt(s1*(s1-a)*(s1-b)*(s1-diag)) + \
       math.sqrt(s2*(s2-c)*(s2-d)*(s2-diag))

print("Area:", area)
