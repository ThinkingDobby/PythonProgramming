import math
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, m = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(n)]

    mv = -math.inf
    mi = mj = -1
    for i in range(n):
        for j in range(m):
            if data[i][j] > mv:
                mv = data[i][j]
                mi = i
                mj = j

    print(max(mi + 1, n - mi) * max(mj + 1, m - mj))