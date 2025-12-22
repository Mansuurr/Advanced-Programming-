n, m = map(int, input().split())
s = input()

arr = []

for i in range(n - m + 1):
    word = s[i:i+m]
    if word not in arr:
        arr.append(word)

print(len(arr))