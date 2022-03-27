import sys

input = sys.stdin.readline

n, m = map(int, input().split())
memo = [False] * (m + 1)

for _ in range(n):
    l, r = map(int, input().split())
    for i in range(l, r + 1):
        memo[i] = True

print(memo[1:].count(False))
for i in range(1, m + 1):
    if not memo[i]:
        print(i, end=' ')
