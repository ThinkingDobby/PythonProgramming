import math
import sys

input = sys.stdin.readline

x, y, n = map(int, input().split())

memo = [math.inf] * (y + 1)
memo[x] = 0

for i in range(x, y + 1):
    if i + n <= y:
        memo[i + n] = min(memo[i + n], memo[i] + 1)
    if i * 2 <= y:
        memo[i * 2] = min(memo[i * 2], memo[i] + 1)
    if i * 3 <= y:
        memo[i * 3] = min(memo[i * 3], memo[i] + 1)

print(memo[y] if memo[y] != math.inf else -1)

