import math
import sys

input = sys.stdin.readline

k = int(input())
memo = [[] for _ in range(k + 1)]

for i in range(1, k + 1):
    tmp = int(math.log2(i)) + 1
    memo[i].append(tmp)
    memo[i] += memo[i - 2**(tmp - 1)]

print(*memo[k])
