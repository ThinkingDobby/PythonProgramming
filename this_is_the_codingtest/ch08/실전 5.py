import sys

n, m = map(int, input().split())
data = [int(input()) for i in range(n)]
memo = [sys.maxsize] * (m + 1)
for i in data:
    if i <= m:
        memo[i] = 1

for i in range(m + 1):
    if memo[i] != sys.maxsize:
        for j in range(n):
                if i + data[j] <= m:
                    memo[i + data[j]] = min(memo[i + data[j]], memo[i] + 1)

print(memo[m] if memo[m] != sys.maxsize else -1)