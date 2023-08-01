import sys

input = sys.stdin.readline

n, m = map(int, input().split())
data = list(map(int, input().split()))

chk = [-1] * n

mv = n
for i in range(m):
    for j in range(data[i] - 1, mv):
        if chk[j] == -1:
            chk[j] = data[i]

    mv = min(data[i], mv)

print(*chk)