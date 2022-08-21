import sys

input = sys.stdin.readline

n, m, sx, sy = map(int, input().split())

print(sx, sy)
for i in range(1, m + 1):
    if i != sy:
        print(sx, i)

flag = 0
for i in range(1, n + 1):
    if i == sx:
        flag = 1
        continue
    if (i + flag) % 2 == 0:
        for j in range(1, m + 1):
            print(i, j)
    else:
        for j in range(m, 0, -1):
            print(i, j)
