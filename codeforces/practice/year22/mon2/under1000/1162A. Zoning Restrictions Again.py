import sys

input = sys.stdin.readline

n, h, m = map(int, input().split())

memo = [h] * (n + 1)
for _ in range(m):
    l, r, x = map(int, input().split())
    for i in range(l, r + 1):
        memo[i] = min(memo[i], x)

print(sum(map(lambda x: x ** 2, memo[1:])))
