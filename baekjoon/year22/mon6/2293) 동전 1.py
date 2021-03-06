import sys

input = sys.stdin.readline

n, m = map(int, input().split())
data = [int(input()) for _ in range(n)]

memo = [0 for _ in range(m + 1)]
memo[0] = 1

for i in data:
    for j in range(i, m + 1):
        memo[j] += memo[j - i]

print(memo[m])