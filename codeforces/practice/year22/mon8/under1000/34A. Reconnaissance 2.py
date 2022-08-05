import math
import sys

input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
data += [data[0]]

mv = math.inf
midx = -1
for i in range(1, n + 1):
    if abs(data[i] - data[i - 1]) < mv:
        mv = abs(data[i] - data[i - 1])
        midx = i

if midx == n:
    print(midx, 1)
else:
    print(midx, midx + 1)