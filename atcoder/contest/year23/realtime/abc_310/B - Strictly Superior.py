import sys

input = sys.stdin.readline

n, m = map(int, input().split())

data = [list(map(int, input().split())) for _ in range(n)]

ans = False
for i in range(n):
    p = data[i][0]
    c = data[i][1]
    check = set(data[i][2:])

    for j in range(n):
        if i == j:
            continue
        pn = data[j][0]
        cn = data[j][1]
        checkn = set(data[j][2:])
        
        l = len(check.intersection(checkn))
        if p < pn and cn == l and c >= cn:
            ans = True
            break
        elif p == pn and cn == l and c > cn:
            ans = True
            break

    if ans:
        break

print("Yes" if ans else "No")