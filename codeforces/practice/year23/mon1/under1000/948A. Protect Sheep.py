import sys

input = sys.stdin.readline

r, c = map(int, input().split())

data = [input().rstrip() for _ in range(r)]

ans = True
for i in range(r):
    for j in range(c):
        if i < r - 1 and ((data[i][j] == "S" and data[i + 1][j] == "W") or (data[i][j] == "W" and data[i + 1][j] == "S")):
            ans = False
            break
        if j < c - 1 and ((data[i][j] == "S" and data[i][j + 1] == "W") or (data[i][j] == "W" and data[i][j + 1] == "S")):
            ans = False
            break

if not ans:
    print("NO")
else:
    print("YES")
    for i in range(r):
        for j in range(c):
            print(data[i][j] if data[i][j] != "." else "D", end='')
        print()
