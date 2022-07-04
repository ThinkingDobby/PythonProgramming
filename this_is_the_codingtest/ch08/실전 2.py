import sys

x = int(input())
memo = [sys.maxsize] * (x + 1)
memo[1] = 0
for i in range(1, x + 1):
    if memo[i] != sys.maxsize:
        if i * 5 <= x:
            memo[i * 5] = min(memo[i * 5], memo[i] + 1)
        if i * 3 <= x:
            memo[i * 3] = min(memo[i * 3], memo[i] + 1)
        if i * 2 <= x:
            memo[i * 2] = min(memo[i * 2], memo[i] + 1)
        if i + 1 <= x:
            memo[i + 1] = min(memo[i + 1], memo[i] + 1)

print(memo[x])