import math
import sys

input = sys.stdin.readline

n = int(input())
memo = [math.inf] * (n + 1)
memo[0] = 0
for i in range(1, n + 1):
    memo[i] = min(memo[i], memo[i - 1] + 1)

    if i * 5 <= n:
        memo[i * 5] = min(memo[i * 5], memo[i] + 1)
    if i * 3 <= n:
        memo[i * 3] = min(memo[i * 3], memo[i] + 1)
    if i * 2 <= n:
        memo[i * 2] = min(memo[i * 2], memo[i] + 1)

print(memo[n] - 1)