import sys

input = sys.stdin.readline

n, k = map(int, input().split())
data = [int(input()) for _ in range(n)]
memo = [0 for _ in range(k + 1)]
memo[0] = 1

for i in data:
    for j in range(i, k + 1):
        memo[j] += memo[j - i]

print(memo[k])