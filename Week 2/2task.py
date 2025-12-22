a = input()
b = input()
k = len(b)
cnt = 0
for i in range(len(a) - k + 1):
    sub = a[i : i + k]
    ok = False
    for j in range(k):
        if sub == b[j:] + b[:j]:
            ok = True
    if ok:
        cnt += 1
print (cnt)