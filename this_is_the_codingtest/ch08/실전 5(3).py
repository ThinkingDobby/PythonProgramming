import sys
import math

input = sys.stdin.readline

n, m = map(int, input().split())
data = [int(input()) for _ in range(n)]

memo = [math.inf] * (m + 1)
for i in data:
    if i <= m:
        memo[i] = 1

for i in range(m + 1):
    for j in data:
        if i + j <= m:
            memo[i + j] = min(memo[i + j], memo[i] + 1)

print(memo[m] if memo[m] != math.inf else -1)

"""
2 15
2
3
5
"""

"""
3 4
3
5
7
"""