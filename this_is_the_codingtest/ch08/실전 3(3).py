import sys

input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
memo = [0] * n

memo[0] = data[0]
memo[1] = data[1]

for i in range(2, n):
    memo[i] = max(memo[i - 1], memo[i - 2] + data[i])

print(memo[-1])

"""
4
1 3 1 5
"""