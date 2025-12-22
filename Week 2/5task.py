letters = "ABCEHKMOPTXY"

n = int(input())
for _ in range(n):
    x = input()

    ok = True
    if len(x) != 6:
        ok = False
    else:
        if x[0] not in letters:
            ok = False
        if not x[1:4].isdigit():
            ok = False
        if x[4] not in letters or x[5] not in letters:
            ok = False

    print("Yes" if ok else "No")