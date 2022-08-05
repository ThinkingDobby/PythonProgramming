import math
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
data = [input().rstrip() for _ in range(n)]

r_min = r_max = c_max = -1
c_min = math.inf

for i in range(n):
    if '*' in data[i]:
        if r_min == -1:
            r_min = i
        r_max = i
        for j in range(m):
            if data[i][j] == '*':
                c_min = min(c_min, j)
                c_max = max(c_max, j)

for i in range(r_min, r_max + 1):
    for j in range(c_min, c_max + 1):
        print(data[i][j], end='')
    print()