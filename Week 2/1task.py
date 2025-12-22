a = input()
answer = 0

for i in range(len(a)):
    if a[i:i+5] == ">>-->":
        answer += 1
    if a[i:i+5] == "<--<<":
        answer += 1

print(answer)
