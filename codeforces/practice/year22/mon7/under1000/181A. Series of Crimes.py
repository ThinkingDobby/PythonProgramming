import sys

input = sys.stdin.readline

n, m = map(int, input().split())
data = [input().rstrip() for _ in range(n)]

x = []
y = []
for i in range(n):
    for j in range(m):
        if data[i][j] == '*':
            x.append(i)
            y.append(j)

ans = []
if x.count(x[0]) == 1:
    ans.append(x[0])
else:
    ans.append(*list(set(x) - {x[0]}))

if y.count(y[0]) == 1:
    ans.append(y[0])
else:
    ans.append(*list(set(y) - {y[0]}))

print(*map(lambda x: x + 1, ans))
