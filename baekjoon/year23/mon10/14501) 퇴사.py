import sys

input = sys.stdin.readline

n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]

memo = [0] * (n + 1)
for i in range(n):
    if i + data[i][0] < n + 1:
        memo[i + data[i][0]] = max(memo[i + data[i][0]], memo[i] + data[i][1])

    memo[i + 1] = max(memo[i + 1], memo[i])

print(memo[-1])
