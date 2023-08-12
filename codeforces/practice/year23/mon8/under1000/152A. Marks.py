import sys

input = sys.stdin.readline

n, m = map(int, input().split())
data = [list(map(int, list(input().rstrip()))) for _ in range(n)]
chk = [False] * n

for j in range(m):
    mv = -1
    for i in range(n):
        mv = max(mv, data[i][j])

    for i in range(n):
        if mv == data[i][j]:
            chk[i] = True

print(chk.count(True))
