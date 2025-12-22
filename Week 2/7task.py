items = input().split()
d = {}

for i in items:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

print("Purchase frequency:")
for k in d:
    print(k + ":", d[k])

mx = 0
best = ""
for k in d:
    if d[k] > mx:
        mx = d[k]
        best = k

print("\nMost popular item:", best)

print("\nPurchased once:", end=" ")
for k in d:
    if d[k] == 1:
        print(k, end=" ")

print("\n\nSorted by frequency:")
for k in sorted(d, key=lambda x: -d[x]):
    print(k, d[k])