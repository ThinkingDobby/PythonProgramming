import math
import sys

input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))

fmv = -1
smv = math.inf
for i in range(1, n):
    fmv = max(data[i] - data[i - 1], fmv)
    if i > 1:
        smv = min(data[i] - data[i - 2], smv)

print(max(fmv, smv))
